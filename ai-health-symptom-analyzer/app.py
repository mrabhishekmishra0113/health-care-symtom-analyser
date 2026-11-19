import os
import re
from flask import Flask, jsonify, render_template, request

try:
    from disease_data import DISEASES_DATABASE
except ImportError:
    DISEASES_DATABASE = {}

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 4096  # 4 KB limit

# ---------------------------------------------------------
# 1. CONFIGURATION & CONSTANTS
# ---------------------------------------------------------
MAX_CONDITION_SUGGESTIONS = 3
MAX_SYMPTOM_TEXT_LENGTH = 500
MAX_SYMPTOMS = 20

SEVERITY_MAP = {
    "mild": 1,
    "moderate": 2,
    "severe": 3,
}

URGENT_SYMPTOMS = {
    "chest pain",
    "shortness of breath",
    "breathing difficulty",
    "coughing blood",
    "fainting",
    "severe abdominal pain",
    "severe upper abdominal pain",
    "severe upper right abdominal pain",
}

EMERGENCY_CONDITIONS = {
    "heart_attack",
    "angina",
    "appendicitis",
    "anaphylaxis",
    "abdominal_aortic_aneurysm",
    "acute_cholecystitis",
    "acute_pancreatitis",
    "blood_poisoning_sepsis",
    "cardiac_arrest",
    "deep_vein_thrombosis",
    "arterial_thrombosis",
}

# ---------------------------------------------------------
# 2. BASE SYMPTOM PROFILES & EXPANDED ALIASES
# ---------------------------------------------------------
BASE_SYMPTOM_PROFILES = {
    "fever": ["viral_infection", "influenza", "pneumonia", "coronavirus_covid_19"],
    "cough": ["common_cold", "influenza", "bronchitis", "pneumonia", "asthma", "allergy"],
    "headache": ["tension_headache", "migraine", "sinusitis", "dehydration", "hypertension"],
    "fatigue": ["viral_infection", "hypothyroidism", "depression", "diabetes", "chronic_fatigue_syndrome"],
    "nausea": ["food_poisoning", "migraine", "gerd", "viral_infection", "gastroenteritis"],
    "shortness of breath": ["heart_attack", "angina", "asthma", "allergy", "pneumonia", "chronic_obstructive_pulmonary_disease"],
    "chest pain": ["heart_attack", "angina", "costochondritis", "gerd", "pneumonia", "chest_and_rib_injury"],
    "dizziness": ["dehydration", "vertigo", "hypertension", "atrial_fibrillation"],
    "sore throat": ["common_cold", "influenza", "catarrh", "coronavirus_covid_19"],
    "rash": ["allergy", "eczema", "chickenpox", "cellulitis"],
    "vomiting": ["food_poisoning", "gastroenteritis", "migraine"],
    "diarrhea": ["gastroenteritis", "food_poisoning", "irritable_bowel_syndrome", "coeliac_disease"],
    "stomach pain": ["food_poisoning", "gastroenteritis", "gallstones", "appendicitis"],
    "abdominal pain": ["irritable_bowel_syndrome", "constipation", "appendicitis", "urinary_tract_infection", "gastroenteritis"],
    "body ache": ["influenza", "viral_infection", "fibromyalgia", "coronavirus_covid_19"],
    "joint pain": ["arthritis", "gout", "viral_infection"],
    "back pain": ["back_problems", "sciatica", "arthritis"],
    "nasal congestion": ["common_cold", "allergy", "sinusitis", "catarrh"],
    "sneezing": ["common_cold", "allergy", "sinusitis"],
    "itchy eyes": ["allergy", "conjunctivitis"],
    "ear pain": ["ear_infection", "sinusitis"],
    "insomnia": ["depression", "bipolar_disorder", "fibromyalgia"],
    "weakness": ["viral_infection", "hypothyroidism", "diabetes", "chronic_fatigue_syndrome"],
    "weakness in foot": ["sciatica", "diabetes", "back_problems"],
    "leg pain": ["sciatica", "deep_vein_thrombosis", "arterial_thrombosis"],
    "foot pain": ["ankle_sprain", "gout", "achilles_tendinopathy", "bunion"],
    "swelling": ["ankle_sprain", "arthritis", "cellulitis", "deep_vein_thrombosis", "gout"],
    "numbness": ["carpal_tunnel_syndrome", "sciatica", "diabetes"],
    "tingling": ["carpal_tunnel_syndrome", "diabetes"],
    "weight loss": ["diabetes", "hyperthyroidism", "depression", "coeliac_disease"],
    "weight gain": ["hypothyroidism", "depression", "binge_eating_disorder"],
    "hair loss": ["alopecia", "hypothyroidism"],
    "skin itching": ["allergy", "eczema", "chickenpox"],
    "dry skin": ["eczema", "hypothyroidism"],
    "anxiety": ["autism", "binge_eating_disorder"],
    "depression": ["depression", "bipolar_disorder"],
    "mood swings": ["bipolar_disorder", "depression"],
    "memory loss": ["alzheimers_disease", "dementia", "concussion"],
    "confusion": ["concussion", "dementia", "alzheimers_disease", "blood_poisoning_sepsis"],
    "difficulty concentrating": ["adhd", "depression", "chronic_fatigue_syndrome"],
    "vision changes": ["hypertension", "brain_tumours", "diabetes"],
    "blurred vision": ["diabetes", "migraine", "conjunctivitis"],
    "eye pain": ["conjunctivitis"],
    "tinnitus": ["ear_infection"],
    "hearing loss": ["ear_infection"],
    "urinary urgency": ["urinary_tract_infection", "benign_prostate_enlargement"],
    "dysuria": ["urinary_tract_infection", "bacterial_vaginosis", "chlamydia"],
    "frequent urination": ["diabetes", "urinary_tract_infection", "benign_prostate_enlargement"],
    "vaginal discharge": ["bacterial_vaginosis", "chlamydia"],
    "pelvic pain": ["endometriosis", "adenomyosis", "urinary_tract_infection", "fibroids"],
    "menstrual cramps": ["adenomyosis", "endometriosis"],
    "heavy bleeding": ["adenomyosis", "fibroids", "endometriosis"],
    "irregular heartbeat": ["atrial_fibrillation"],
    "heart palpitations": ["atrial_fibrillation"],
    "high blood pressure": ["hypertension", "chronic_kidney_disease"],
    "low blood pressure": ["dehydration", "addisons_disease"],
    "constipation": ["constipation", "irritable_bowel_syndrome", "hypothyroidism"],
    "bloating": ["irritable_bowel_syndrome", "constipation", "coeliac_disease"],
    "gas": ["irritable_bowel_syndrome", "constipation"],
    "acid reflux": ["gerd"],
    "heartburn": ["gerd"],
    "indigestion": ["gerd", "gallstones"],
    "bad breath": ["dental_abscess"],
    "tooth pain": ["dental_abscess"],
    "persistent cough": ["bronchitis", "chronic_obstructive_pulmonary_disease", "bronchiectasis", "catarrh"],
    "coughing blood": ["bronchiectasis"],
    "wheezing": ["asthma", "chronic_obstructive_pulmonary_disease"],
    "breathing difficulty": ["asthma", "anaphylaxis", "pneumonia"],
    "chest tightness": ["angina", "asthma", "costochondritis", "heart_attack"],
    "shoulder pain": ["frozen_shoulder", "cervical_spondylosis", "heart_attack"],
    "neck stiffness": ["cervical_spondylosis", "tension_headache", "ankylosing_spondylitis"],
    "neck pain": ["cervical_spondylosis", "tension_headache", "frozen_shoulder"],
    "lower back pain": ["sciatica", "back_problems", "ankylosing_spondylitis"],
    "upper back pain": ["back_problems"],
    "knee pain": ["arthritis"],
    "hip pain": ["arthritis"],
    "elbow pain": ["arthritis"],
    "wrist pain": ["carpal_tunnel_syndrome", "arthritis"],
    "hand numbness": ["carpal_tunnel_syndrome"],
    "finger tingling": ["carpal_tunnel_syndrome", "diabetes"],
    "tremor": ["ataxia"],
    "balance problems": ["vertigo", "ataxia", "brain_tumours"],
    "vertigo": ["vertigo", "migraine"],
    "lightheadedness": ["dehydration"],
    "fainting": ["anaphylaxis", "epilepsy", "cardiac_arrest"],
    "cold hands and feet": ["hypothyroidism", "anorexia_nervosa", "arterial_thrombosis"],
    "bruising easily": ["ankle_sprain", "acute_lymphoblastic_leukaemia", "acute_myeloid_leukaemia"],
    "nosebleed": ["hypertension"],
    "excessive sweating": ["heart_attack"],
    "fever and chills": ["influenza", "pneumonia", "blood_poisoning_sepsis"],
    "malaise": ["viral_infection", "chickenpox"],
}

# Expanded real-world synonyms so natural user inputs match accurately
SYMPTOM_ALIASES = {
    "fever": ["high temperature", "temperature", "hot", "chills", "bukhar"],
    "cough": ["coughing", "dry cough", "productive cough", "wet cough", "khansi"],
    "headache": ["head ache", "head pain", "head hurting", "throbbing head", "sir dard"],
    "fatigue": ["tired", "tiredness", "exhaustion", "exhausted", "low energy", "lethargy"],
    "nausea": ["nauseated", "queasy", "feeling sick", "urge to vomit", "ji machlana"],
    "vomiting": ["throwing up", "vomit", "puking", "ulti"],
    "shortness of breath": ["short of breath", "breathless", "out of breath", "wheeze", "gasping"],
    "breathing difficulty": ["trouble breathing", "cannot breathe", "hard to breathe", "difficulty breathing", "saans fulna"],
    "chest pain": ["pain in chest", "pain in my chest", "chest discomfort", "chest ache", "heart pain"],
    "chest tightness": ["tightness in chest", "heavy chest", "chest pressure", "pressure in chest"],
    "dizziness": ["dizzy", "feeling faint", "woozy", "chakkar"],
    "vertigo": ["room spinning", "head spinning", "spinning sensation"],
    "sore throat": ["throat pain", "throat irritation", "scratchy throat", "painful swallowing", "gala kharab"],
    "rash": ["skin rash", "red spots", "hives", "red patches", "skin bumps"],
    "skin itching": ["itchy skin", "itching", "scratching", "khujli"],
    "diarrhea": ["loose motions", "loose motion", "runny stool", "watery stool", "dast"],
    "constipation": ["hard stool", "hard stools", "can't poop", "irregular bowel", "kabz"],
    "stomach pain": ["belly pain", "tummy ache", "stomach ache", "gastric pain", "pet dard"],
    "abdominal pain": ["lower belly pain", "cramps", "abdominal cramps", "lower abdominal pain"],
    "severe abdominal pain": ["unbearable stomach pain", "severe belly pain", "sharp abdominal pain"],
    "heartburn": ["acidity", "burning chest", "acid burning", "chest burn"],
    "acid reflux": ["sour burps", "regurgitation", "acid coming up"],
    "bloating": ["bloated", "full stomach", "swollen belly", "heavy stomach"],
    "gas": ["flatulence", "passing gas", "farting", "trapped gas"],
    "body ache": ["body pain", "muscle ache", "muscle pain", "sore muscles", "aching body"],
    "joint pain": ["arthritis pain", "aching joints", "stiff joints", "joint ache"],
    "back pain": ["backache", "back ache", "sore back", "kamar dard"],
    "lower back pain": ["lumbar pain", "pain in lower back"],
    "neck pain": ["sore neck", "pain in neck", "cervical pain"],
    "neck stiffness": ["stiff neck", "cannot turn neck"],
    "shoulder pain": ["sore shoulder", "pain in shoulder", "stiff shoulder"],
    "knee pain": ["sore knee", "pain in knee", "aching knees"],
    "foot pain": ["heel pain", "ankle pain", "sore feet", "pain in foot", "toe pain"],
    "nasal congestion": ["stuffy nose", "blocked nose", "congestion", "runny nose", "cold nose"],
    "sneezing": ["sneeze", "frequent sneezing"],
    "itchy eyes": ["eye irritation", "red eyes", "watery eyes", "pink eye", "burning eyes"],
    "blurred vision": ["blurry vision", "fuzzy vision", "trouble seeing clearly"],
    "ear pain": ["earache", "ear hurting", "pain in ear", "ear ache"],
    "tinnitus": ["ringing in ears", "buzzing in ear"],
    "insomnia": ["sleeplessness", "can't sleep", "sleep trouble", "difficulty sleeping", "no sleep"],
    "tooth pain": ["toothache", "tooth ache", "dental pain", "gum pain", "cavity pain"],
    "dysuria": ["burning urination", "painful urination", "burning pee", "pain when peeing"],
    "frequent urination": ["peeing a lot", "urinating often", "frequent peeing"],
    "urinary urgency": ["urgent need to pee", "cannot hold urine"],
    "menstrual cramps": ["period cramps", "period pain", "painful periods"],
    "heavy bleeding": ["heavy periods", "excessive menstrual bleeding"],
    "hair loss": ["hair thinning", "bald patches", "hair fall", "losing hair"],
    "pimples": ["acne", "zits", "breakouts", "spots on face"],
    "heart palpitations": ["racing heart", "fast heartbeat", "pounding heart", "heart fluttering"],
    "hand numbness": ["numb hands", "numb fingers", "pins and needles in hand"],
    "tremor": ["shaking hands", "shaky hands", "trembling"],
    "gum bleeding": ["bleeding gums"],
    "fainting": ["passed out", "blackout", "loss of consciousness"],
}

# ---------------------------------------------------------
# 3. AUTO-SYNC DATABASE & PRE-COMPILE REGEX
# ---------------------------------------------------------
DISEASE_PROFILES = dict(DISEASES_DATABASE)
SYMPTOM_PROFILES = {k: list(v) for k, v in BASE_SYMPTOM_PROFILES.items()}

# Automatically register every symptom from DISEASES_DATABASE into SYMPTOM_PROFILES
SEVERITY_RANK = {"low": 1, "moderate": 2, "emergency": 3}

for disease_key, info in DISEASE_PROFILES.items():
    for raw_sym in info.get("symptoms", []):
        norm_sym = raw_sym.strip().lower()
        if not norm_sym:
            continue
        disease_list = SYMPTOM_PROFILES.setdefault(norm_sym, [])
        if disease_key not in disease_list:
            disease_list.append(disease_key)

# Sort each symptom's disease list so common/mild conditions appear before rare emergencies
for sym, keys in SYMPTOM_PROFILES.items():
    keys.sort(
        key=lambda k: SEVERITY_RANK.get(
            DISEASE_PROFILES.get(k, {}).get("severity_level", "moderate"), 2
        )
    )

ALIAS_LOOKUP = {canonical: canonical for canonical in SYMPTOM_PROFILES}
for canonical, aliases in SYMPTOM_ALIASES.items():
    if canonical in SYMPTOM_PROFILES:
        for alias in aliases:
            ALIAS_LOOKUP.setdefault(alias.lower(), canonical)

SORTED_ALIASES = sorted(ALIAS_LOOKUP.keys(), key=len, reverse=True)
COMPILED_ALIAS_PATTERNS = [
    (alias, ALIAS_LOOKUP[alias], re.compile(rf"(?<!\w){re.escape(alias)}(?!\w)"))
    for alias in SORTED_ALIASES
]
AND_ALIASES = [alias for alias in SORTED_ALIASES if " and " in alias]

NEGATION_REGEX = re.compile(
    r"\b(?:no|neither|not(?!\s+only\b)|without|denies|denying|negative\s+for|never|"
    r"don't|doesn't|didn't|haven't|hasn't|isn't|aren't)(?:\s+\w+){0,2}\s*$"
)
FILLER_WORDS_REGEX = re.compile(
    r"\b(i have|i am having|i'm having|have|feeling|feel|having|suffering from|with|experiencing|my)\b"
)
SPLIT_CONNECTORS_REGEX = re.compile(
    r"(\s*(?:[,;/]|\band\b|\bor\b|\bnor\b|\bplus\b|\bbut\b|\bhowever\b)\s*)"
)


# ---------------------------------------------------------
# 4. CORE NLP & SCORING FUNCTIONS
# ---------------------------------------------------------
def find_symptom_match(symptom_text: str):
    cleaned = re.sub(r"[^a-z0-9\s]", " ", symptom_text.strip().lower())
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if not cleaned:
        return None
    if cleaned in ALIAS_LOOKUP:
        return ALIAS_LOOKUP[cleaned]

    matches = []
    for alias, canonical, pattern in COMPILED_ALIAS_PATTERNS:
        match = pattern.search(cleaned)
        if match:
            matches.append((match.start(), -len(alias), canonical))

    return min(matches)[2] if matches else None


def _is_negated_symptom(prefix: str) -> bool:
    return bool(NEGATION_REGEX.search(prefix.strip()))


def extract_symptoms(symptoms_text: str) -> list[str]:
    if not symptoms_text or not str(symptoms_text).strip():
        return []

    text = str(symptoms_text).lower().replace("&", " and ").replace("+", " and ")
    text = FILLER_WORDS_REGEX.sub(" ", text)
    text = re.sub(r"^\s*symptoms?\s*(?:of\b)?", " ", text)
    text = re.sub(r"[^a-z0-9\s,;\n/'-]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Protect multi-word aliases containing "and" (e.g., "fever and chills", "cold hands and feet")
    for alias in AND_ALIASES:
        text = re.sub(
            re.escape(alias),
            lambda m: re.sub(r"\band\b", "\x00", m.group()),
            text,
        )

    candidates = SPLIT_CONNECTORS_REGEX.split(text)
    ordered = []
    seen = set()
    inherited_negation = False
    last_candidate_negated = False

    for index, candidate in enumerate(candidates):
        if index % 2:
            connector = candidate.strip()
            inherited_negation = connector in {"or", "nor", ","} and last_candidate_negated
            continue

        candidate = re.sub(r"\s+", " ", candidate.replace("\x00", "and")).strip()
        if not candidate:
            continue

        if re.search(r"\b(yes|only|just|actually)\b", candidate):
            inherited_negation = False

        matches = []
        for _, canonical, pattern in COMPILED_ALIAS_PATTERNS:
            for match in pattern.finditer(candidate):
                matches.append((match.start(), match.end(), canonical))

        matches.sort(key=lambda item: (item[0], -(item[1] - item[0])))
        selected = []
        for start, end, canonical in matches:
            if any(start < s_end and end > s_start for s_start, s_end, _ in selected):
                continue
            selected.append((start, end, canonical))

        negated_matches = [_is_negated_symptom(candidate[:start]) for start, _, _ in selected]
        parsed = [
            canonical
            for (_, _, canonical), is_negated in zip(selected, negated_matches)
            if not is_negated and not inherited_negation
        ]

        last_candidate_negated = inherited_negation or (bool(selected) and all(negated_matches))
        if not parsed and selected:
            continue
        if not parsed:
            parsed = [candidate]

        for symptom in parsed:
            if symptom not in seen:
                ordered.append(symptom)
                seen.add(symptom)

    return ordered


def _get_condition_profile(condition_key: str, suppress_meds: bool = False) -> dict:
    profile = DISEASE_PROFILES.get(condition_key, {})
    is_emergency = (
        condition_key in EMERGENCY_CONDITIONS
        or profile.get("severity_level") == "emergency"
    )
    return {
        "disease_name": profile.get(
            "disease_name",
            condition_key.replace("_", " ").replace("'", "").title(),
        ),
        "severity_level": profile.get("severity_level", "moderate"),
        "symptoms": profile.get("symptoms") or [],
        "why": profile.get(
            "why",
            "This is a possible condition associated with the reported symptom(s), but it cannot be assessed from symptoms alone.",
        ),
        "medicines": [] if (suppress_meds or is_emergency) else (profile.get("medicines") or []),
        "home_remedies": profile.get("home_remedies") or [],
        "critical_conditions": profile.get("critical_conditions") or [],
        "doctor_advice": profile.get(
            "doctor_advice",
            "Consult a qualified healthcare professional for assessment.",
        ),
        "doctor_type": profile.get("doctor_type", ""),
    }


def _score_disease_match(disease_key: str, symptoms_list: list[str]) -> int:
    profile = DISEASE_PROFILES.get(disease_key, {})
    disease_symptoms = {s.strip().lower() for s in (profile.get("symptoms") or [])}
    score = 0

    for raw_symptom in symptoms_list:
        canonical = find_symptom_match(raw_symptom)
        if canonical and canonical in disease_symptoms:
            score += 12
        elif canonical and disease_key in SYMPTOM_PROFILES.get(canonical, []):
            score += 8

    # Slightly penalize rare/emergency diseases unless urgent symptoms are present
    sev = profile.get("severity_level", "moderate")
    if sev == "emergency":
        score -= 4
    elif sev == "low":
        score += 2

    return score


def analyze_symptoms(symptoms_text: str, severity_text: str) -> dict:
    if symptoms_text is None:
        symptoms_text = ""
    elif not isinstance(symptoms_text, str):
        raise TypeError("Symptoms must be provided as text.")

    symptoms = extract_symptoms(symptoms_text)
    severity = str(severity_text or "moderate").lower().strip() or "moderate"
    if severity not in SEVERITY_MAP:
        raise ValueError("Severity must be mild, moderate, or severe.")
    score = SEVERITY_MAP[severity]

    if not symptoms:
        return {
            "summary": (
                "Please enter at least one symptom."
                if not symptoms_text.strip()
                else "No current symptoms were recognized. Try common terms like fever, cough, headache, acidity, or back pain."
            ),
            "matched_conditions": {},
            "recognized_symptom_count": 0,
            "unmatched_symptoms": [],
            "urgent_symptoms": False,
            "condition_suggestions": [],
            "why_explanations": [],
            "medicine_suggestions": [],
            "home_remedies": [],
            "doctor_advice": [],
            "recommendations": ["Enter symptoms you are currently experiencing for analysis."],
        }

    candidate_scores = {}
    symptom_candidates = {}
    unmatched_symptoms = []
    candidate_order = 0

    for symptom in symptoms:
        canonical = find_symptom_match(symptom)
        candidate_keys = SYMPTOM_PROFILES.get(canonical, []) if canonical else []
        if not candidate_keys:
            unmatched_symptoms.append(symptom)
            continue

        symptom_candidates[symptom] = candidate_keys
        for pos, condition_key in enumerate(candidate_keys):
            candidate = candidate_scores.setdefault(
                condition_key,
                {"symptom_matches": set(), "first_order": candidate_order, "profile_preference": 0},
            )
            candidate_order += 1
            candidate["symptom_matches"].add(canonical)
            candidate["profile_preference"] += max(0, 10 - pos)

    recognized_symptoms = list(symptom_candidates)
    recognized_canonicals = {find_symptom_match(s) for s in recognized_symptoms}
    urgent_symptoms = bool(recognized_canonicals & URGENT_SYMPTOMS)

    ranked_condition_keys = sorted(
        candidate_scores,
        key=lambda k: (
            0 if urgent_symptoms and k == "heart_attack" else 1,
            -len(candidate_scores[k]["symptom_matches"]),
            -_score_disease_match(k, recognized_symptoms),
            -candidate_scores[k]["profile_preference"],
            candidate_scores[k]["first_order"],
        ),
    )[:MAX_CONDITION_SUGGESTIONS]

    top_condition_key = ranked_condition_keys[0] if ranked_condition_keys else None
    is_top_emergency = (
        DISEASE_PROFILES.get(top_condition_key, {}).get("severity_level") == "emergency"
        if top_condition_key else False
    )
    show_emergency = urgent_symptoms or is_top_emergency

    matched_conditions = {}
    for symptom, candidate_keys in symptom_candidates.items():
        matched_conditions[symptom] = [
            _get_condition_profile(k, suppress_meds=show_emergency)
            for k in ranked_condition_keys
            if k in candidate_keys
        ]

    for symptom in unmatched_symptoms:
        matched_conditions[symptom] = [{
            "disease_name": "No clear match",
            "why": "The symptom could not be mapped to a known condition.",
            "medicines": [],
            "home_remedies": [],
            "doctor_advice": "Try a simpler symptom description or consult a doctor.",
        }]

    condition_suggestions = [
        _get_condition_profile(k)["disease_name"] for k in ranked_condition_keys
    ]

    # Collect remedies & medicines ONLY from top 2 matched conditions to keep advice focused & non-repetitive
    why_explanations = []
    medicine_suggestions = []
    home_remedies = []
    doctor_advices = []

    for condition_key in ranked_condition_keys[:2]:
        cond = _get_condition_profile(condition_key, suppress_meds=show_emergency)
        why_explanations.append(f"{cond['disease_name']}: {cond['why']}")
        if not show_emergency:
            medicine_suggestions.extend(cond.get("medicines", []))
        home_remedies.extend(cond.get("home_remedies", []))
        if cond.get("doctor_advice"):
            doctor_advices.append(f"{cond['disease_name']}: {cond['doctor_advice']}")

    why_explanations = list(dict.fromkeys(why_explanations))[:3]
    medicine_suggestions = list(dict.fromkeys(medicine_suggestions))[:5]
    home_remedies = list(dict.fromkeys(home_remedies))[:5]
    doctor_advices = list(dict.fromkeys(doctor_advices))[:2]

    if recognized_symptoms:
        summary = (
            f"Recognized {len(recognized_symptoms)} symptom(s) with {severity} severity. "
            f"Showing up to {MAX_CONDITION_SUGGESTIONS} closest possibilities; "
            "this is informational guidance, not a medical diagnosis."
        )
    else:
        summary = (
            "No supported symptoms were recognized. Try common terms like fever, cough, "
            "headache, acidity, or joint pain."
        )

    recommendations = [
        "This tool provides informational guidance only and is not a medical diagnosis.",
    ]

    if show_emergency:
        recommendations.insert(
            0,
            "URGENT: Some symptoms or top matches suggest a potentially serious condition. Seek immediate medical care.",
        )
    elif not recognized_symptoms:
        recommendations.insert(
            0,
            "Describe the specific symptoms you are feeling (for example: 'sore throat and mild fever').",
        )
    elif score >= 3:
        recommendations.insert(0, "Since you marked severity as severe, consult a doctor promptly.")
    elif score == 2:
        recommendations.insert(0, "Monitor your symptoms over the next 24-48 hours and consult a doctor if they persist.")
    else:
        recommendations.insert(0, "Follow targeted self-care measures and rest. Most mild symptoms improve within a few days.")

    return {
        "summary": summary,
        "matched_conditions": matched_conditions,
        "recognized_symptom_count": len(recognized_symptoms),
        "unmatched_symptoms": unmatched_symptoms,
        "urgent_symptoms": show_emergency,
        "condition_suggestions": condition_suggestions,
        "why_explanations": why_explanations,
        "medicine_suggestions": medicine_suggestions,
        "home_remedies": home_remedies,
        "doctor_advice": doctor_advices,
        "recommendations": recommendations,
    }


# ---------------------------------------------------------
# 5. FLASK ROUTES
# ---------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a valid JSON object."}), 400

    symptoms = data.get("symptoms")
    if not isinstance(symptoms, str):
        return jsonify({"error": "The 'symptoms' field is required and must be a string."}), 400
    if len(symptoms) > MAX_SYMPTOM_TEXT_LENGTH:
        return jsonify({"error": f"Symptoms must be {MAX_SYMPTOM_TEXT_LENGTH} characters or fewer."}), 400

    severity = data.get("severity", "moderate")
    if not isinstance(severity, str) or severity.strip().lower() not in SEVERITY_MAP:
        return jsonify({"error": "Severity must be mild, moderate, or severe."}), 400

    if len(extract_symptoms(symptoms)) > MAX_SYMPTOMS:
        return jsonify({"error": f"Enter no more than {MAX_SYMPTOMS} symptoms at a time."}), 400

    return jsonify(analyze_symptoms(symptoms, severity))


@app.errorhandler(413)
def request_entity_too_large(_error):
    return jsonify({"error": "Request body must be 4 KB or smaller."}), 413


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, host="127.0.0.1", port=5000, use_reloader=False)