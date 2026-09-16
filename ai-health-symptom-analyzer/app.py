import re

from flask import Flask, render_template, request, jsonify
from disease_data import DISEASES_DATABASE

app = Flask(__name__)

symptom_profiles = {
    "fever": ["viral_infection", "bacterial_infection", "influenza", "pneumonia", "strep_throat"],
    "cough": ["common_cold", "influenza", "bronchitis", "pneumonia", "asthma", "allergy", "respiratory_infection"],
    "headache": ["tension_headache", "migraine", "sinusitis", "stress_headache", "dehydration", "hypertension"],
    "fatigue": ["sleep_deprivation", "anemia", "viral_infection", "hypothyroidism", "depression", "diabetes"],
    "nausea": ["food_poisoning", "migraine", "acid_reflux", "viral_infection", "gastritis"],
    "shortness of breath": ["heart_attack", "heart_stress", "asthma", "allergy", "respiratory_infection", "anxiety", "pneumonia"],
    "chest pain": ["heart_attack", "heart_stress", "muscle_strain", "acid_reflux", "anxiety", "pneumonia"],
    "dizziness": ["low_blood_pressure", "dehydration", "vertigo", "anemia", "hypoglycemia"],
    "sore throat": ["common_cold", "strep_throat", "allergy", "influenza", "tonsillitis"],
    "rash": ["allergy", "contact_dermatitis", "skin_allergy", "rash_infection", "urticaria"],
    "vomiting": ["food_poisoning", "gastroenteritis", "migraine", "motion_sickness"],
    "diarrhea": ["gastroenteritis", "food_poisoning", "irritable_bowel", "medication_side_effect"],
    "stomach pain": ["gastritis", "acid_reflux", "food_poisoning", "appendicitis", "irritable_bowel"],
    "abdominal pain": ["gastritis", "appendicitis", "irritable_bowel", "urinary_tract_infection"],
    "body ache": ["influenza", "viral_infection", "fibromyalgia", "dehydration"],
    "joint pain": ["arthritis", "gout", "injury", "viral_infection"],
    "back pain": ["muscle_strain", "sciatica", "injury", "arthritis"],
    "nasal congestion": ["common_cold", "allergy", "sinusitis", "influenza"],
    "sneezing": ["common_cold", "allergy", "sinusitis"],
    "itchy eyes": ["allergy", "conjunctivitis"],
    "ear pain": ["ear_infection", "sinusitis", "jaw_strain"],
    "insomnia": ["stress_headache", "sleep_deprivation", "anxiety", "depression"],
    "weakness": ["anemia", "depression", "hypothyroidism", "diabetes", "viral_infection", "malnutrition"],
    "weakness in foot": ["sciatica", "peripheral_neuropathy", "anemia", "diabetes", "back_problems"],
    "muscle weakness": ["muscular_dystrophy", "myasthenia_gravis", "anemia", "hypothyroidism"],
    "leg pain": ["sciatica", "arthritis", "back_problems", "deep_vein_thrombosis"],
    "foot pain": ["arthritis", "gout", "plantar_heel_pain", "ankle_sprain"],
    "swelling": ["edema", "arthritis", "cellulitis", "allergy"],
    "numbness": ["peripheral_neuropathy", "carpal_tunnel_syndrome", "sciatica", "diabetes"],
    "tingling": ["carpal_tunnel_syndrome", "peripheral_neuropathy", "anxiety", "diabetes"],
    "weight loss": ["diabetes", "cancer", "hyperthyroidism", "depression", "malabsorption"],
    "weight gain": ["hypothyroidism", "depression", "diabetes"],
    "hair loss": ["alopecia", "stress", "nutritional_deficiency", "thyroid_disease"],
    "hair loss alopecia": ["alopecia", "stress", "iron_deficiency"],
    "skin itching": ["allergy", "eczema", "urticaria", "psoriasis"],
    "dry skin": ["eczema", "hypothyroidism", "malnutrition"],
    "burning sensation": ["neuropathy", "acid_reflux", "dermatitis"],
    "anxiety": ["anxiety_disorder", "panic_disorder", "depression", "hyperthyroidism"],
    "panic": ["panic_disorder", "anxiety_disorder", "heart_palpitations"],
    "depression": ["depression", "bipolar_disorder", "hypothyroidism"],
    "mood swings": ["bipolar_disorder", "depression", "pms"],
    "memory loss": ["dementia", "depression", "stress"],
    "confusion": ["delirium", "dementia", "diabetes", "hypoglycemia"],
    "difficulty concentrating": ["adhd", "depression", "anxiety", "sleep_deprivation"],
    "vision changes": ["diabetes", "hypertension", "eye_disease"],
    "blurred vision": ["diabetes", "eye_strain", "migraine"],
    "eye pain": ["conjunctivitis", "glaucoma", "eye_strain"],
    "tinnitus": ["hearing_loss", "ear_infection", "hypertension"],
    "hearing loss": ["hearing_loss", "ear_infection", "aging"],
    "hoarseness": ["laryngitis", "vocal_strain", "throat_cancer"],
    "voice loss": ["laryngitis", "vocal_strain"],
    "urinary urgency": ["urinary_tract_infection", "diabetes", "prostate_issues"],
    "dysuria": ["urinary_tract_infection", "sexually_transmitted_infection"],
    "frequent urination": ["diabetes", "urinary_tract_infection", "prostate_issues"],
    "vaginal discharge": ["bacterial_vaginosis", "yeast_infection", "sexually_transmitted_infection"],
    "pelvic pain": ["endometriosis", "pelvic_inflammatory_disease", "urinary_tract_infection"],
    "menstrual cramps": ["dysmenorrhea", "endometriosis"],
    "heavy bleeding": ["fibroids", "adenomyosis", "clotting_disorder"],
    "irregular heartbeat": ["atrial_fibrillation", "heart_disease", "anxiety"],
    "heart palpitations": ["palpitations", "anxiety", "hyperthyroidism"],
    "high blood pressure": ["hypertension", "stress", "kidney_disease"],
    "low blood pressure": ["hypotension", "dehydration", "anemia"],
    "high cholesterol": ["hyperlipidemia", "metabolic_syndrome"],
    "constipation": ["irritable_bowel_syndrome", "dehydration", "hypothyroidism"],
    "bloating": ["irritable_bowel_syndrome", "lactose_intolerance", "celiac_disease"],
    "gas": ["irritable_bowel_syndrome", "lactose_intolerance", "food_intolerance"],
    "acid reflux": ["gerd", "hiatus_hernia", "stress"],
    "heartburn": ["gerd", "peptic_ulcer"],
    "indigestion": ["gerd", "peptic_ulcer", "irritable_bowel_syndrome"],
    "mouth ulcer": ["aphthous_ulcer", "oral_thrush", "vitamin_deficiency"],
    "bad breath": ["gum_disease", "tooth_decay", "acid_reflux"],
    "tooth pain": ["tooth_decay", "dental_abscess", "tooth_sensitivity"],
    "gum bleeding": ["gum_disease", "vitamin_k_deficiency"],
    "swollen glands": ["glandular_fever", "lymphoma", "infection"],
    "lymph node enlargement": ["infection", "cancer", "lymphoma"],
    "persistent cough": ["tuberculosis", "chronic_bronchitis", "lung_cancer"],
    "coughing blood": ["tuberculosis", "lung_cancer", "bronchiectasis"],
    "wheezing": ["asthma", "copd", "heart_failure"],
    "breathing difficulty": ["asthma", "pneumonia", "heart_disease"],
    "chest tightness": ["angina", "anxiety", "asthma"],
    "shoulder pain": ["rotator_cuff_injury", "arthritis", "heart_disease"],
    "neck stiffness": ["meningitis", "cervical_spondylosis", "tension"],
    "neck pain": ["cervical_spondylosis", "muscle_strain", "arthritis"],
    "lower back pain": ["sciatica", "muscle_strain", "herniated_disc"],
    "upper back pain": ["muscle_strain", "arthritis", "tension"],
    "knee pain": ["osteoarthritis", "meniscus_tear", "ligament_injury"],
    "hip pain": ["hip_arthritis", "labral_tear", "bursitis"],
    "elbow pain": ["golfers_elbow", "tennis_elbow", "arthritis"],
    "wrist pain": ["carpal_tunnel_syndrome", "arthritis", "wrist_strain"],
    "hand numbness": ["carpal_tunnel_syndrome", "peripheral_neuropathy"],
    "finger tingling": ["carpal_tunnel_syndrome", "diabetes"],
    "tremor": ["parkinson's_disease", "hyperthyroidism", "anxiety"],
    "shaking hands": ["parkinson's_disease", "essential_tremor", "hyperthyroidism"],
    "balance problems": ["vertigo", "inner_ear_disease", "neurological_disorder"],
    "vertigo": ["vertigo", "inner_ear_disease", "migraine"],
    "lightheadedness": ["low_blood_pressure", "anemia", "dehydration"],
    "fainting": ["syncope", "arrhythmia", "low_blood_pressure"],
    "cold hands and feet": ["poor_circulation", "hypothyroidism", "raynaud_disease"],
    "bruising easily": ["bleeding_disorder", "vitamin_k_deficiency", "leukemia"],
    "bleeding gums": ["gum_disease", "vitamin_k_deficiency", "bleeding_disorder"],
    "nosebleed": ["hypertension", "blood_clotting_disorder", "nasal_polyp"],
    "excessive sweating": ["hyperthyroidism", "anxiety", "hyperhidrosis"],
    "night sweats": ["tuberculosis", "lymphoma", "menopause"],
    "fever and chills": ["infection", "malaria", "viral_infection"],
    "flu-like symptoms": ["influenza", "viral_infection", "lyme_disease"],
    "malaise": ["viral_infection", "depression", "malnutrition"]
}


disease_profiles = {
    "viral_infection": {
        "disease_name": "Viral infection",
        "why": "Fever and fatigue often occur when the body is fighting a virus.",
        "medicines": ["Paracetamol for fever", "Ibuprofen for pain"],
        "home_remedies": ["Rest", "Drink warm fluids", "Use a humidifier"],
        "doctor_advice": "If fever lasts more than 3 days or symptoms worsen, consult a doctor."
    },
    "bacterial_infection": {
        "disease_name": "Bacterial infection",
        "why": "High fever can indicate the immune system is responding to bacteria.",
        "medicines": ["Follow your doctor’s prescription", "Antibiotics only when prescribed"],
        "home_remedies": ["Stay hydrated", "Eat light, nutritious meals"],
        "doctor_advice": "See a doctor to confirm the infection and get the correct antibiotics."
    },
    "influenza": {
        "disease_name": "Flu (Influenza)",
        "why": "Fever, cough, sore throat, and body ache are common with the flu.",
        "medicines": ["Antiviral tablets if prescribed", "Paracetamol for fever"],
        "home_remedies": ["Rest completely", "Drink soups and fluids", "Gargle warm salt water"],
        "doctor_advice": "Visit a doctor if breathing becomes difficult or if symptoms are severe."
    },
    "pneumonia": {
        "disease_name": "Pneumonia",
        "why": "Fever, cough, chest pain, and shortness of breath can signal a lung infection.",
        "medicines": ["Antibiotics when prescribed", "Cough relief medication"],
        "home_remedies": ["Get plenty of rest", "Stay hydrated", "Use a warm compress on the chest"],
        "doctor_advice": "See a doctor urgently if you have high fever, difficulty breathing, or chest pain."
    },
    "common_cold": {
        "disease_name": "Common cold",
        "why": "A mild viral infection of the upper respiratory tract often causes cough and sore throat.",
        "medicines": ["Cough syrup", "Lozenges", "Paracetamol for discomfort"],
        "home_remedies": ["Steam inhalation", "Warm teas with honey", "Rest"],
        "doctor_advice": "See a doctor if symptoms last more than 10 days or worsen."
    },
    "bronchitis": {
        "disease_name": "Bronchitis",
        "why": "Cough and mucus can occur when the bronchial tubes are inflamed.",
        "medicines": ["Cough expectorant", "Anti-inflammatory medication as advised"],
        "home_remedies": ["Steam inhalation", "Warm fluid intake", "Avoid cold air"],
        "doctor_advice": "Consult a doctor if you have high fever or difficulty breathing."
    },
    "asthma": {
        "disease_name": "Asthma",
        "why": "Wheezing and shortness of breath can indicate airway sensitivity or asthma.",
        "medicines": ["Inhaler as prescribed", "Bronchodilator medication"],
        "home_remedies": ["Stay away from triggers", "Practice deep breathing exercises"],
        "doctor_advice": "See a specialist if breathlessness persists or worsens."
    },
    "allergy": {
        "disease_name": "Allergic reaction",
        "why": "Rash, cough, and sore throat can appear when the body reacts to an allergen.",
        "medicines": ["Antihistamines", "Cough drops"],
        "home_remedies": ["Avoid the allergen", "Drink plenty of water", "Use saline nasal rinse"],
        "doctor_advice": "Consult a doctor for allergy testing and long-term management."
    },
    "sinusitis": {
        "disease_name": "Sinusitis",
        "why": "Headache, facial pressure, and nasal congestion can happen when sinuses are inflamed.",
        "medicines": ["Decongestants", "Pain relief tablets"],
        "home_remedies": ["Nasal saline rinse", "Warm compress over sinuses", "Drink fluids"],
        "doctor_advice": "Visit a doctor if symptoms last more than a week or become severe."
    },
    "tension_headache": {
        "disease_name": "Tension headache",
        "why": "Stress and muscle tension can cause a dull headache across the head.",
        "medicines": ["Paracetamol", "Ibuprofen"],
        "home_remedies": ["Apply a warm compress", "Rest in a quiet room", "Practice relaxation"],
        "doctor_advice": "Visit a doctor if headaches are frequent or severe."
    },
    "migraine": {
        "disease_name": "Migraine",
        "why": "A migraine is a neurological headache that may cause nausea and light sensitivity.",
        "medicines": ["Migraine-specific medication if prescribed", "Pain reliever tablets"],
        "home_remedies": ["Rest in a dark place", "Use cold packs", "Stay hydrated"],
        "doctor_advice": "See a doctor for persistent migraine or if nausea is severe."
    },
    "stress_headache": {
        "disease_name": "Stress-related headache",
        "why": "Stress and poor sleep often lead to headache and fatigue.",
        "medicines": ["Pain relief tablets"],
        "home_remedies": ["Practice relaxation", "Improve sleep habits", "Stay hydrated"],
        "doctor_advice": "Consult a doctor if stress-related headaches continue."
    },
    "dehydration": {
        "disease_name": "Dehydration",
        "why": "Not drinking enough fluids can cause dizziness, fatigue, and headache.",
        "medicines": ["Oral rehydration salts"],
        "home_remedies": ["Drink water frequently", "Include electrolytes", "Rest in shade"],
        "doctor_advice": "If dehydration is severe, seek medical help immediately."
    },
    "hypertension": {
        "disease_name": "High blood pressure",
        "why": "Headache and dizziness may occur when blood pressure is elevated.",
        "medicines": ["Blood pressure medication if prescribed"],
        "home_remedies": ["Reduce salt intake", "Practice stress management"],
        "doctor_advice": "See a doctor for blood pressure monitoring and treatment."
    },
    "heart_attack": {
        "disease_name": "Heart Attack (Emergency)",
        "why": "A blocked coronary artery can reduce blood flow to the heart muscle, causing crushing chest pain, pressure, nausea, and breathlessness.",
        "medicines": ["Aspirin only if already advised and safe for you", "Nitroglycerin only if prescribed", "Emergency heart medicines in hospital"],
        "home_remedies": ["Sit upright and stay calm", "Do not drive yourself", "Call emergency services immediately"],
        "critical_conditions": ["Cardiac arrest", "Shock", "Severe breathing difficulty"],
        "doctor_advice": "Call emergency services now. This is a medical emergency. Seek immediate hospital care and urgent cardiology evaluation.",
        "doctor_type": "Emergency Medicine, Cardiologist"
    },
    "heart_stress": {
        "disease_name": "Heart Stress / Angina",
        "why": "The heart may be under strain when the blood supply is limited, causing pressure, tightness, or pain in the chest.",
        "medicines": ["Nitroglycerin only if prescribed", "Aspirin only when appropriate and advised"],
        "home_remedies": ["Stop exertion", "Sit down and rest", "Avoid heavy activity"],
        "critical_conditions": ["Heart attack", "Unstable angina"],
        "doctor_advice": "Urgent medical evaluation is needed if chest pain is severe, new, or comes with shortness of breath; seek emergency consultation immediately.",
        "doctor_type": "Cardiologist, Emergency Medicine"
    },
    "hypoglycemia": {
        "disease_name": "Low blood sugar",
        "why": "Dizziness and weakness can occur when blood sugar drops too low.",
        "medicines": ["Follow doctor advice"],
        "home_remedies": ["Eat a small sugary snack", "Drink juice", "Rest"],
        "doctor_advice": "Consult a doctor if symptoms recur frequently."
    },
    "hypothyroidism": {
        "disease_name": "Hypothyroidism",
        "why": "Fatigue and cold sensitivity may result from low thyroid function.",
        "medicines": ["Thyroid hormone replacement only if prescribed"],
        "home_remedies": ["Eat iodine-rich foods", "Stay warm"],
        "doctor_advice": "Talk to a doctor for a thyroid test."
    },
    "depression": {
        "disease_name": "Depression",
        "why": "Fatigue, insomnia, and low mood can be signs of depression.",
        "medicines": ["Medication only if prescribed"],
        "home_remedies": ["Talk to someone you trust", "Maintain a routine", "Get gentle exercise"],
        "doctor_advice": "Consult a mental health professional if symptoms persist."
    },
    "diabetes": {
        "disease_name": "Diabetes",
        "why": "Fatigue, frequent urination, and thirst can happen when blood sugar is too high.",
        "medicines": ["Medication only if prescribed"],
        "home_remedies": ["Manage diet", "Stay active"],
        "doctor_advice": "See a doctor for blood sugar testing and management."
    },
    "gastritis": {
        "disease_name": "Gastritis",
        "why": "Stomach pain and nausea can occur when the stomach lining is irritated.",
        "medicines": ["Antacids", "Stomach protectants"],
        "home_remedies": ["Eat mild foods", "Avoid spicy meals", "Stay hydrated"],
        "doctor_advice": "Visit a doctor if pain is severe or continues."
    },
    "tonsillitis": {
        "disease_name": "Tonsillitis",
        "why": "A sore throat with swelling can be caused by inflamed tonsils.",
        "medicines": ["Pain relievers", "Antibiotics only if prescribed"],
        "home_remedies": ["Gargle salt water", "Drink warm liquids"],
        "doctor_advice": "See a doctor for diagnosis and treatment."
    },
    "urticaria": {
        "disease_name": "Urticaria (Hives)",
        "why": "Raised itchy red bumps usually happen from an allergic reaction.",
        "medicines": ["Antihistamines"],
        "home_remedies": ["Cool compresses", "Avoid scratching"],
        "doctor_advice": "Seek medical advice if the rash is widespread or breathing is affected."
    },
    "gastroenteritis": {
        "disease_name": "Gastroenteritis",
        "why": "Diarrhea, nausea, and vomiting are often caused by a stomach infection.",
        "medicines": ["Oral rehydration salts", "Antiemetic medication if prescribed"],
        "home_remedies": ["Sip clear fluids", "Eat bland foods", "Rest"],
        "doctor_advice": "See a doctor if dehydration or bloody diarrhea occurs."
    },
    "irritable_bowel": {
        "disease_name": "Irritable Bowel Syndrome",
        "why": "Abdominal pain and diarrhea can occur with a sensitive digestive tract.",
        "medicines": ["Antispasmodics", "Fiber supplements"],
        "home_remedies": ["Eat smaller meals", "Avoid trigger foods"],
        "doctor_advice": "Consult a doctor for a proper IBS diagnosis."
    },
    "medication_side_effect": {
        "disease_name": "Medication side effect",
        "why": "Diarrhea or nausea can occur after starting a new medicine.",
        "medicines": ["Discuss with your doctor before changing medication"],
        "home_remedies": ["Stay hydrated", "Eat light foods"],
        "doctor_advice": "Contact your doctor if side effects are severe."
    },
    "appendicitis": {
        "disease_name": "Appendicitis",
        "why": "Sharp abdominal pain on the right side can indicate appendix inflammation.",
        "medicines": ["Do not take painkillers before diagnosis"],
        "home_remedies": ["Avoid eating or drinking until evaluated"],
        "doctor_advice": "Seek immediate medical attention if appendicitis is suspected."
    },
    "urinary_tract_infection": {
        "disease_name": "Urinary tract infection",
        "why": "Lower abdominal pain and discomfort can accompany a UTI.",
        "medicines": ["Antibiotics only when prescribed"],
        "home_remedies": ["Drink plenty of water", "Avoid irritants"],
        "doctor_advice": "See a doctor for a urine test and treatment."
    },
    "fibromyalgia": {
        "disease_name": "Fibromyalgia",
        "why": "Widespread body ache and fatigue can be due to fibromyalgia.",
        "medicines": ["Pain management medication if prescribed"],
        "home_remedies": ["Gentle exercise", "Good sleep habits", "Relaxation"],
        "doctor_advice": "Consult a doctor if unexplained body aches continue."
    },
    "arthritis": {
        "disease_name": "Arthritis",
        "why": "Joint pain and stiffness often point to arthritis.",
        "medicines": ["Anti-inflammatory medication if prescribed"],
        "home_remedies": ["Rest the joint", "Apply heat or cold"],
        "doctor_advice": "See a doctor for diagnosis and joint care advice."
    },
    "gout": {
        "disease_name": "Gout",
        "why": "Sudden joint pain can be caused by high uric acid in the body.",
        "medicines": ["Pain relief"],
        "home_remedies": ["Avoid rich foods", "Stay hydrated"],
        "doctor_advice": "Consult a doctor if joint pain is severe or recurring."
    },
    "injury": {
        "disease_name": "Injury",
        "why": "Pain after movement or trauma can be caused by a strain or injury.",
        "medicines": ["Pain relievers"],
        "home_remedies": ["Rest", "Ice the affected area"],
        "doctor_advice": "See a doctor for severe or persistent pain."
    },
    "sciatica": {
        "disease_name": "Sciatica",
        "why": "Back pain that travels down the leg can be due to nerve compression.",
        "medicines": ["Pain relief medication if prescribed"],
        "home_remedies": ["Gentle stretching", "Rest"],
        "doctor_advice": "Consult a doctor if pain is severe or causes numbness."
    },
    "conjunctivitis": {
        "disease_name": "Conjunctivitis",
        "why": "Red, itchy eyes often happen with eye inflammation due to infection or allergy.",
        "medicines": ["Eye drops if prescribed"],
        "home_remedies": ["Keep eyes clean", "Use warm compresses"],
        "doctor_advice": "See a doctor if eye irritation persists."
    },
    "ear_infection": {
        "disease_name": "Ear infection",
        "why": "Ear pain can occur when fluid or infection affects the middle ear.",
        "medicines": ["Pain relievers", "Antibiotics only when prescribed"],
        "home_remedies": ["Warm compress"],
        "doctor_advice": "Visit a doctor for an ear exam and treatment."
    },
    "jaw_strain": {
        "disease_name": "Jaw strain",
        "why": "Jaw or ear pain may come from teeth grinding or jaw tension.",
        "medicines": ["Pain relievers"],
        "home_remedies": ["Relax the jaw", "Avoid hard foods"],
        "doctor_advice": "See a doctor if pain is severe or does not improve."
    },
    "stress": {
        "disease_name": "Stress",
        "why": "Physical symptoms may appear when stress affects the body.",
        "medicines": ["Relaxation techniques"],
        "home_remedies": ["Meditation", "Healthy routine", "Rest"],
        "doctor_advice": "Talk to a doctor if stress affects daily life."
    }
}

# Merge with comprehensive disease database
disease_profiles.update(DISEASES_DATABASE)

symptom_aliases = {
    "fever": ["fever", "high temperature", "temperature", "hot", "chills"],
    "cough": ["cough", "coughing", "dry cough", "productive cough"],
    "headache": ["headache", "head ache", "head pain", "migraine", "sinus pressure"],
    "fatigue": ["fatigue", "tired", "tiredness", "exhaustion", "weakness"],
    "nausea": ["nausea", "nauseated", "vomit", "vomiting", "queasy"],
    "shortness of breath": ["shortness of breath", "breathless", "difficulty breathing", "cannot breathe", "wheeze"],
    "chest pain": ["chest pain", "chest discomfort", "tightness in chest"],
    "dizziness": ["dizziness", "dizzy", "lightheaded", "vertigo"],
    "sore throat": ["sore throat", "throat pain", "throat irritation", "scratchy throat"],
    "rash": ["rash", "skin rash", "red spots", "hives", "itchy skin"],
    "vomiting": ["vomiting", "throwing up", "vomit", "puking"],
    "diarrhea": ["diarrhea", "loose motions", "runny stool"],
    "stomach pain": ["stomach pain", "belly pain", "abdominal pain", "tummy ache"],
    "body ache": ["body ache", "body pain", "muscle ache", "ache"],
    "joint pain": ["joint pain", "knee pain", "elbow pain", "arthritis pain"],
    "back pain": ["back pain", "lower back pain", "upper back pain"],
    "nasal congestion": ["nasal congestion", "stuffy nose", "blocked nose", "congestion"],
    "sneezing": ["sneezing", "sneeze"],
    "itchy eyes": ["itchy eyes", "eye irritation", "red eyes"],
    "ear pain": ["ear pain", "earache", "ear hurting"],
    "insomnia": ["insomnia", "sleeplessness", "can't sleep", "sleep trouble"]
}

alias_lookup = {}
for canonical, aliases in symptom_aliases.items():
    for alias in aliases:
        alias_lookup[alias] = canonical

severity_map = {
    "mild": 1,
    "moderate": 2,
    "severe": 3
}


def find_symptom_match(symptom_text):
    symptom = re.sub(r"[^a-z0-9\s]", " ", symptom_text.strip().lower())
    symptom = re.sub(r"\s+", " ", symptom).strip()
    if not symptom:
        return None
    if symptom in alias_lookup:
        return alias_lookup[symptom]

    for alias, canonical in alias_lookup.items():
        if alias in symptom or symptom in alias:
            return canonical
    return None


def extract_symptoms(symptoms_text):
    if not symptoms_text or not str(symptoms_text).strip():
        return []

    text = str(symptoms_text).lower()
    text = text.replace("&", " and ")
    text = text.replace("+", " and ")
    text = re.sub(r"\b(i have|have|feeling|feel|having|symptoms?|suffering from|with)\b", " ", text)
    text = re.sub(r"[^a-z0-9\s,;\n/]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    candidates = []
    for delimiter in [",", ";", "\n", " / ", " and "]:
        if delimiter in text:
            for piece in text.split(delimiter):
                cleaned = re.sub(r"\b(and|or|plus)\b", " ", piece).strip()
                if cleaned:
                    candidates.append(cleaned)
            break
    else:
        candidates = [text]

    ordered = []
    seen = set()
    for item in candidates:
        for segment in re.split(r"\s+", item):
            segment = segment.strip()
            if not segment:
                continue
            canonical = find_symptom_match(segment)
            if canonical and canonical not in seen:
                ordered.append(canonical)
                seen.add(canonical)
            elif segment not in seen:
                ordered.append(segment)
                seen.add(segment)

    if not ordered:
        return [text]

    normalized = []
    for item in ordered:
        cleaned = re.sub(r"\s+", " ", str(item)).strip()
        if cleaned and cleaned not in normalized:
            normalized.append(cleaned)
    return normalized


def _score_disease_match(disease_key, symptoms_list):
    profile = disease_profiles.get(disease_key, {})
    disease_text = " ".join(profile.get("symptoms", [])).lower()
    score = 0

    for raw_symptom in symptoms_list:
        symptom = re.sub(r"[^a-z0-9\s]", " ", raw_symptom.lower())
        symptom = re.sub(r"\s+", " ", symptom).strip()
        if not symptom:
            continue
        canonical = find_symptom_match(symptom)
        if canonical and disease_key in symptom_profiles.get(canonical, []):
            score += 10

        if symptom in disease_text or disease_text.find(symptom) != -1:
            score += 4

        if canonical and canonical in disease_text:
            score += 2

    if profile.get("critical_conditions"):
        score -= 1

    return score


def analyze_symptoms(symptoms_text, severity_text):
    symptoms = extract_symptoms(symptoms_text)
    severity = severity_text.lower().strip() or "moderate"
    score = severity_map.get(severity, 2)

    if not symptoms:
        return {
            "summary": "Please enter at least one symptom.",
            "recommendations": ["Provide comma-separated symptoms for analysis."]
        }

    matched_conditions = {}
    for symptom in symptoms:
        canonical = find_symptom_match(symptom)
        if canonical:
            candidate_keys = symptom_profiles.get(canonical, [])
            conditions = []
            for condition_key in candidate_keys:
                condition_profile = disease_profiles.get(condition_key)
                if condition_profile:
                    score_value = _score_disease_match(condition_key, symptoms)
                    ranked_profile = dict(condition_profile)
                    ranked_profile["_score"] = score_value
                    conditions.append(ranked_profile)
                else:
                    conditions.append({
                        "disease_name": condition_key.replace('_', ' ').title(),
                        "why": "This condition is recognized but has no detailed profile.",
                        "medicines": [],
                        "home_remedies": [],
                        "doctor_advice": "Consult a healthcare provider for accurate guidance.",
                        "_score": 1
                    })
        else:
            conditions = [{
                "disease_name": "No clear match",
                "why": "The symptom could not be mapped to a known condition.",
                "medicines": [],
                "home_remedies": [],
                "doctor_advice": "Try a different symptom description or consult a doctor.",
                "_score": 0
            }]

        conditions.sort(key=lambda item: item.get("_score", 0), reverse=True)
        matched_conditions[symptom] = [
            {k: v for k, v in condition.items() if k != "_score"}
            for condition in conditions[:5]
        ]

    condition_suggestions = []
    seen_conditions = set()
    for conditions in matched_conditions.values():
        for condition in conditions:
            if condition.get("disease_name") and condition["disease_name"] not in seen_conditions:
                seen_conditions.add(condition["disease_name"])
                condition_suggestions.append(condition["disease_name"])

    rank_scores = {}
    for symptom in matched_conditions:
        for condition in matched_conditions[symptom]:
            if condition.get("disease_name"):
                key = condition["disease_name"]
                rank_scores[key] = rank_scores.get(key, 0) + 1

    condition_suggestions = sorted(
        seen_conditions,
        key=lambda name: (-rank_scores.get(name, 0), name)
    )

    why_explanations = []
    medicine_suggestions = []
    home_remedies = []
    doctor_advices = []

    for conditions in matched_conditions.values():
        for condition in conditions:
            if condition.get("disease_name"):
                if condition["why"] not in why_explanations:
                    why_explanations.append(condition["why"])
                for med in condition["medicines"]:
                    if med not in medicine_suggestions:
                        medicine_suggestions.append(med)
                for remedy in condition["home_remedies"]:
                    if remedy not in home_remedies:
                        home_remedies.append(remedy)
                if condition["doctor_advice"] not in doctor_advices:
                    doctor_advices.append(condition["doctor_advice"])

    summary = (
        f"Detected {len(symptoms)} symptom(s) with {severity} severity. "
        "Review the matched conditions, possible reasons, and suggested next steps below."
    )

    recommendations = [
        "This is a guidance tool only and not a substitute for medical diagnosis.",
        "If symptoms worsen or become severe, seek urgent medical care.",
        "Stay hydrated and rest as much as possible."
    ]

    if score >= 3:
        recommendations.insert(0, "This looks like a high-severity case. Contact a doctor promptly.")
    elif score == 2:
        recommendations.insert(0, "Watch the symptoms closely and consult a physician if they persist.")
    else:
        recommendations.insert(0, "Monitor the symptoms and rest. Most mild cases improve with self-care.")

    return {
        "summary": summary,
        "matched_conditions": matched_conditions,
        "condition_suggestions": condition_suggestions[:8],
        "why_explanations": why_explanations[:8],
        "medicine_suggestions": medicine_suggestions[:12],
        "home_remedies": home_remedies[:12],
        "doctor_advice": doctor_advices[:6],
        "recommendations": recommendations
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    symptoms = data.get("symptoms", "")
    severity = data.get("severity", "moderate")
    result = analyze_symptoms(symptoms, severity)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
