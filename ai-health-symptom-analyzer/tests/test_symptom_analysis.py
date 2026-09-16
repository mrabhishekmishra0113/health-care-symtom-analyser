import unittest

from app import analyze_symptoms


class SymptomAnalysisTests(unittest.TestCase):
    def test_parses_natural_language_symptoms(self):
        result = analyze_symptoms("I have fever and cough and headache", "moderate")

        self.assertIn("fever", result["matched_conditions"])
        self.assertIn("cough", result["matched_conditions"])
        self.assertIn("headache", result["matched_conditions"])

    def test_counts_multiple_symptoms(self):
        result = analyze_symptoms("fever, cough, headache", "mild")

        self.assertIn("Detected 3 symptom(s)", result["summary"])

    def test_prioritizes_relevant_conditions(self):
        result = analyze_symptoms("fever, cough, sore throat", "moderate")

        self.assertIn("Flu (Influenza)", result["condition_suggestions"][:3])
        self.assertNotIn("Viral infection", result["condition_suggestions"][:3])


if __name__ == "__main__":
    unittest.main()
