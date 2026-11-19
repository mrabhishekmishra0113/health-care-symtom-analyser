import unittest

import app as app_module
from app import analyze_symptoms, app, extract_symptoms

# Backward-compatible reference regardless of uppercase/lowercase naming in app.py
SYMPTOM_PROFILES = getattr(
    app_module,
    "SYMPTOM_PROFILES",
    getattr(app_module, "symptom_profiles", {}),
)


class SymptomAnalysisTests(unittest.TestCase):
    def test_homepage_and_static_stylesheet_are_available(self):
        client = app.test_client()

        homepage = client.get("/")
        stylesheet = client.get("/static/styles.css")

        self.assertEqual(homepage.status_code, 200)
        self.assertIn('href="/static/styles.css"', homepage.get_data(as_text=True))
        self.assertIn('const analyzeUrl = "/analyze";', homepage.get_data(as_text=True))
        self.assertEqual(stylesheet.status_code, 200)
        stylesheet.close()

    def test_analyze_endpoint_returns_json(self):
        response = app.test_client().post(
            "/analyze",
            json={"symptoms": "fever, cough", "severity": "moderate"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("summary", response.get_json())

    def test_analyze_endpoint_rejects_invalid_requests(self):
        client = app.test_client()

        malformed = client.post(
            "/analyze",
            data="{bad json",
            content_type="application/json",
        )
        missing_symptoms = client.post("/analyze", json={"severity": "mild"})
        non_object = client.post("/analyze", json=["fever"])
        non_string_symptoms = client.post("/analyze", json={"symptoms": ["fever"]})
        invalid_severity = client.post(
            "/analyze",
            json={"symptoms": "fever", "severity": "critical"},
        )
        too_many_symptoms = client.post(
            "/analyze",
            json={"symptoms": ", ".join(["fever"] + [f"unknown{i}" for i in range(20)])},
        )
        too_long = client.post(
            "/analyze",
            json={"symptoms": "x" * 501},
        )
        oversized_body = client.post(
            "/analyze",
            data=" " * 5000,
            content_type="application/json",
        )

        self.assertEqual(malformed.status_code, 400)
        self.assertEqual(missing_symptoms.status_code, 400)
        self.assertEqual(non_object.status_code, 400)
        self.assertEqual(non_string_symptoms.status_code, 400)
        self.assertEqual(invalid_severity.status_code, 400)
        self.assertEqual(too_many_symptoms.status_code, 400)
        self.assertEqual(too_long.status_code, 400)
        self.assertEqual(oversized_body.status_code, 413)
        self.assertIn("error", oversized_body.get_json())

    def test_empty_analysis_returns_complete_safe_shape(self):
        result = analyze_symptoms(" ", "mild")

        self.assertEqual(result["matched_conditions"], {})
        self.assertEqual(result["condition_suggestions"], [])
        self.assertIn("Please enter", result["summary"])

    def test_analysis_rejects_unknown_severity(self):
        with self.assertRaisesRegex(ValueError, "Severity must be"):
            analyze_symptoms("fever", "critical")

    def test_parses_natural_language_symptoms(self):
        result = analyze_symptoms("I have fever and cough and headache", "moderate")

        self.assertIn("fever", result["matched_conditions"])
        self.assertIn("cough", result["matched_conditions"])
        self.assertIn("headache", result["matched_conditions"])

    def test_preserves_multiword_symptoms_without_false_matches(self):
        result = analyze_symptoms("I have a fever and stomach pain", "moderate")

        self.assertEqual(
            list(result["matched_conditions"]),
            ["fever", "stomach pain"],
        )

    def test_parses_multiword_symptoms_from_comma_separated_input(self):
        result = analyze_symptoms("shortness of breath, chest pain", "severe")

        self.assertEqual(
            list(result["matched_conditions"]),
            ["shortness of breath", "chest pain"],
        )

    def test_recognizes_common_chest_and_breathing_phrases(self):
        extracted = extract_symptoms("pain in my chest and trouble breathing")
        self.assertIn("chest pain", extracted)
        self.assertTrue(
            "shortness of breath" in extracted or "breathing difficulty" in extracted
        )

    def test_does_not_treat_negated_symptoms_as_current_symptoms(self):
        self.assertEqual(
            extract_symptoms("I do not have fever, but I have a cough"),
            ["cough"],
        )
        self.assertEqual(extract_symptoms("without fever"), [])
        self.assertEqual(extract_symptoms("no cough or fever"), [])
        self.assertEqual(extract_symptoms("neither cough nor fever"), [])
        self.assertEqual(extract_symptoms("no cough but fever"), ["fever"])

        result = analyze_symptoms("no fever", "mild")
        self.assertEqual(result["recognized_symptom_count"], 0)
        self.assertIn("No current symptoms", result["summary"])

    def test_parses_symptoms_from_the_full_symptom_profile_list(self):
        result = analyze_symptoms("weight loss", "moderate")

        self.assertEqual(result["recognized_symptom_count"], 1)
        self.assertTrue(result["condition_suggestions"])
        self.assertTrue(result["matched_conditions"]["weight loss"])

    def test_extracts_every_configured_canonical_symptom(self):
        for symptom in SYMPTOM_PROFILES:
            with self.subTest(symptom=symptom):
                self.assertEqual(extract_symptoms(symptom), [symptom])

    def test_does_not_claim_unrecognized_text_was_analyzed(self):
        result = analyze_symptoms("blargh", "mild")

        self.assertEqual(result["recognized_symptom_count"], 0)
        self.assertFalse(result["condition_suggestions"])
        self.assertIn("No supported symptoms", result["summary"])

    def test_unrecognized_symptoms_are_not_counted_as_supported(self):
        result = analyze_symptoms("fever, blargh", "moderate")

        self.assertEqual(result["recognized_symptom_count"], 1)
        self.assertEqual(result["unmatched_symptoms"], ["blargh"])

    def test_counts_multiple_symptoms(self):
        result = analyze_symptoms("fever, cough, headache", "mild")

        self.assertEqual(result["recognized_symptom_count"], 3)
        self.assertIn("3", result["summary"])

    def test_prioritizes_relevant_conditions(self):
        result = analyze_symptoms("fever, cough, sore throat", "moderate")

        self.assertIn("Flu (Influenza)", result["condition_suggestions"][:3])

    def test_limits_results_to_three_relevant_conditions(self):
        result = analyze_symptoms("fever, cough, headache", "moderate")
        displayed_conditions = [
            condition["disease_name"]
            for conditions in result["matched_conditions"].values()
            for condition in conditions
        ]

        self.assertLessEqual(len(result["condition_suggestions"]), 3)
        self.assertLessEqual(len(set(displayed_conditions)), 3)
        self.assertIn("Flu (Influenza)", result["condition_suggestions"])

    def test_keeps_emergency_condition_in_limited_results(self):
        result = analyze_symptoms("chest pain", "severe")

        self.assertIn(
            "Heart Attack (Emergency)",
            result["condition_suggestions"],
        )
        self.assertLessEqual(len(result["condition_suggestions"]), 3)

    def test_urgent_symptoms_override_mild_severity_in_guidance(self):
        result = analyze_symptoms(
            "chest pain, fever, cough, headache",
            "mild",
        )

        self.assertTrue(result["urgent_symptoms"])
        self.assertIn("Heart Attack (Emergency)", result["condition_suggestions"])
        self.assertTrue(
            "urgent" in result["recommendations"][0].lower()
            or "emergency" in result["recommendations"][0].lower()
        )

    def test_remedies_are_specific_and_not_bloated(self):
        result = analyze_symptoms("heartburn, acid reflux", "mild")

        self.assertLessEqual(len(result["home_remedies"]), 5)
        self.assertFalse(result["urgent_symptoms"])
        self.assertTrue(any("2-3 hours" in r or "bed" in r.lower() for r in result["home_remedies"]))

    def test_emergency_suppresses_self_medication_suggestions(self):
        result = analyze_symptoms("chest pain, shortness of breath", "severe")

        self.assertTrue(result["urgent_symptoms"])
        self.assertEqual(result["medicine_suggestions"], [])


if __name__ == "__main__":
    unittest.main()