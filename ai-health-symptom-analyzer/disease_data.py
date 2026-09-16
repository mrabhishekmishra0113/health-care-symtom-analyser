# Comprehensive disease database with all medical information
DISEASES_DATABASE = {
    "abdominal_aortic_aneurysm": {
        "disease_name": "Abdominal Aortic Aneurysm",
        "symptoms": ["severe abdominal pain", "back pain", "chest pain"],
        "why": "The abdominal aorta weakens and balloons, causing severe pain and potential rupture.",
        "medicines": ["Pain management medications", "Blood pressure control medications"],
        "home_remedies": ["Complete bed rest", "Avoid heavy lifting"],
        "critical_conditions": ["Severe tearing pain", "Sudden collapse", "Heavy bleeding"],
        "doctor_advice": "Seek emergency care immediately. This is a life-threatening condition.",
        "doctor_type": "Vascular Surgeon, Cardiologist"
    },
    "achilles_tendinopathy": {
        "disease_name": "Achilles Tendinopathy",
        "symptoms": ["heel pain", "back of leg pain", "difficulty walking"],
        "why": "The Achilles tendon becomes inflamed or degenerates from overuse.",
        "medicines": ["Anti-inflammatory medications", "Pain relievers"],
        "home_remedies": ["Rest and ice", "Stretching exercises", "Elevation"],
        "critical_conditions": ["Complete tendon rupture", "Inability to walk"],
        "doctor_advice": "Rest and avoid strenuous activity. Seek physical therapy if pain persists.",
        "doctor_type": "Orthopedist, Physical Therapist"
    },
    "acne": {
        "disease_name": "Acne",
        "symptoms": ["pimples", "blackheads", "whiteheads", "oily skin"],
        "why": "Excess sebum production, bacteria, and clogged pores cause acne formation.",
        "medicines": ["Benzoyl peroxide", "Salicylic acid products", "Retinoids", "Antibiotics (if infected)"],
        "home_remedies": ["Keep skin clean", "Use oil-free moisturizer", "Avoid touching face", "Eat healthy diet"],
        "critical_conditions": ["Severe cystic acne", "Signs of infection"],
        "doctor_advice": "Consult a dermatologist if acne is severe or leaving scars.",
        "doctor_type": "Dermatologist"
    },
    "acute_cholecystitis": {
        "disease_name": "Acute Cholecystitis",
        "symptoms": ["severe upper right abdominal pain", "nausea", "vomiting", "fever"],
        "why": "The gallbladder becomes inflamed, usually due to gallstones blocking the cystic duct.",
        "medicines": ["Pain management", "Antibiotics if infected", "Anti-nausea medications"],
        "home_remedies": ["NPO (nothing by mouth)", "Bed rest"],
        "critical_conditions": ["Perforation of gallbladder", "Peritonitis", "Sepsis"],
        "doctor_advice": "Seek immediate medical attention. May require surgical intervention.",
        "doctor_type": "Surgeon, Gastroenterologist"
    },
    "acute_lymphoblastic_leukaemia": {
        "disease_name": "Acute Lymphoblastic Leukaemia (ALL)",
        "symptoms": ["fatigue", "fever", "bruising easily", "frequent infections", "bone pain"],
        "why": "Rapid multiplication of immature lymphoid cells disrupts normal blood cell production.",
        "medicines": ["Chemotherapy regimens", "Targeted therapy", "Supportive care medications"],
        "home_remedies": ["Nutritious diet", "Rest", "Hygiene precautions"],
        "critical_conditions": ["Severe infection", "Bleeding", "Organ failure"],
        "doctor_advice": "Seek immediate oncology care. This requires aggressive treatment.",
        "doctor_type": "Oncologist, Hematologist"
    },
    "acute_myeloid_leukaemia": {
        "disease_name": "Acute Myeloid Leukaemia (AML)",
        "symptoms": ["fatigue", "fever", "shortness of breath", "bleeding tendency", "bruising"],
        "why": "Rapid growth of abnormal myeloid cells in bone marrow prevents normal blood production.",
        "medicines": ["Intensive chemotherapy", "Targeted therapies", "Stem cell transplant"],
        "home_remedies": ["Balanced nutrition", "Rest and sleep", "Infection prevention"],
        "critical_conditions": ["Severe infections", "Internal bleeding", "DIC"],
        "doctor_advice": "Requires immediate hospitalization and specialized cancer treatment.",
        "doctor_type": "Oncologist, Hematologist"
    },
    "acute_pancreatitis": {
        "disease_name": "Acute Pancreatitis",
        "symptoms": ["severe upper abdominal pain", "nausea", "vomiting", "fever"],
        "why": "Pancreatic enzymes activate prematurely, causing pancreas inflammation.",
        "medicines": ["Pain management", "Antibiotics if infected", "Digestive enzyme inhibitors"],
        "home_remedies": ["NPO initially", "IV fluids", "Bed rest"],
        "critical_conditions": ["Severe pancreatitis", "Organ failure", "Infection"],
        "doctor_advice": "Seek emergency medical care immediately.",
        "doctor_type": "Gastroenterologist, Surgeon"
    },
    "acute_respiratory_infection_ari": {
        "disease_name": "Acute Respiratory Infection (ARI)",
        "symptoms": ["cough", "fever", "sore throat", "runny nose", "shortness of breath"],
        "why": "Viral or bacterial infection affects the respiratory tract.",
        "medicines": ["Cough suppressants", "Pain relievers", "Antibiotics if bacterial"],
        "home_remedies": ["Steam inhalation", "Warm fluids", "Rest", "Honey and lemon"],
        "critical_conditions": ["Severe breathing difficulty", "Cyanosis"],
        "doctor_advice": "See a doctor if symptoms last more than a week or worsen.",
        "doctor_type": "Pulmonologist, General Practitioner"
    },
    "addisons_disease": {
        "disease_name": "Addison's Disease",
        "symptoms": ["fatigue", "weakness", "low blood pressure", "skin darkening", "weight loss"],
        "why": "Adrenal glands don't produce enough cortisol and aldosterone.",
        "medicines": ["Cortisol replacement", "Aldosterone replacement", "Emergency hydrocortisone"],
        "home_remedies": ["Maintain salt intake", "Balanced diet", "Stress management"],
        "critical_conditions": ["Addisonian crisis", "Severe shock", "Hypoglycemia"],
        "doctor_advice": "Requires lifelong hormone replacement therapy and regular monitoring.",
        "doctor_type": "Endocrinologist"
    },
    "adenomyosis": {
        "disease_name": "Adenomyosis",
        "symptoms": ["severe menstrual cramps", "heavy menstrual bleeding", "pelvic pain"],
        "why": "Uterine lining grows into the muscle wall, causing inflammation.",
        "medicines": ["NSAIDs for pain", "Hormonal contraceptives", "Progestins"],
        "home_remedies": ["Heat therapy", "Regular exercise", "Dietary changes"],
        "critical_conditions": ["Severe bleeding leading to anemia"],
        "doctor_advice": "Consult a gynecologist for proper diagnosis and treatment options.",
        "doctor_type": "Gynecologist"
    },
    "alcohol_related_liver_disease": {
        "disease_name": "Alcohol-Related Liver Disease",
        "symptoms": ["fatigue", "jaundice", "abdominal swelling", "nausea", "yellowing of skin"],
        "why": "Alcohol damages liver cells over time, causing inflammation and cirrhosis.",
        "medicines": ["Liver protective medications", "Vitamins", "Corticosteroids"],
        "home_remedies": ["Complete alcohol abstinence", "High protein diet", "Rest"],
        "critical_conditions": ["Liver failure", "Hepatic coma", "Internal bleeding"],
        "doctor_advice": "Stop alcohol consumption immediately and seek hepatology care.",
        "doctor_type": "Hepatologist, Gastroenterologist"
    },
    "allergic_rhinitis": {
        "disease_name": "Allergic Rhinitis",
        "symptoms": ["nasal congestion", "sneezing", "itchy nose", "runny nose", "postnasal drip"],
        "why": "Immune system overreacts to environmental allergens affecting nasal passages.",
        "medicines": ["Antihistamines", "Nasal corticosteroids", "Decongestants"],
        "home_remedies": ["Saline nasal rinse", "Avoid allergens", "Keep windows closed"],
        "critical_conditions": ["Anaphylaxis if severe allergy"],
        "doctor_advice": "Identify and avoid triggers. Consider allergy testing.",
        "doctor_type": "Allergist, ENT Specialist"
    },
    "allergies": {
        "disease_name": "Allergies",
        "symptoms": ["itching", "rash", "swelling", "sneezing", "watery eyes"],
        "why": "Immune system reacts to normally harmless substances.",
        "medicines": ["Antihistamines", "Corticosteroids", "Epinephrine for severe"],
        "home_remedies": ["Avoid triggers", "Cool compresses", "Saline rinse"],
        "critical_conditions": ["Anaphylaxis", "Severe swelling", "Breathing difficulty"],
        "doctor_advice": "Get allergy testing done to identify specific triggers.",
        "doctor_type": "Allergist, Immunologist"
    },
    "alopecia_hair_loss": {
        "disease_name": "Alopecia (Hair Loss)",
        "symptoms": ["hair thinning", "bald patches", "receding hairline", "scalp itching"],
        "why": "Hair follicles shrink or are attacked by immune system.",
        "medicines": ["Minoxidil", "Finasteride", "Corticosteroid injections"],
        "home_remedies": ["Hair massage", "Scalp care", "Nutritious diet", "Stress reduction"],
        "critical_conditions": ["Complete baldness in severe cases"],
        "doctor_advice": "Consult a dermatologist for diagnosis and treatment options.",
        "doctor_type": "Dermatologist, Trichologist"
    },
    "alzheimers_disease": {
        "disease_name": "Alzheimer's Disease",
        "symptoms": ["memory loss", "confusion", "difficulty with tasks", "behavioral changes"],
        "why": "Progressive brain cell death causes cognitive decline.",
        "medicines": ["Cholinesterase inhibitors", "Memantine", "Symptom management drugs"],
        "home_remedies": ["Cognitive exercises", "Social engagement", "Healthy diet"],
        "critical_conditions": ["Severe dementia", "Inability to care for self"],
        "doctor_advice": "Requires ongoing neurologist care and family support planning.",
        "doctor_type": "Neurologist, Geriatrician"
    },
    "anal_cancer": {
        "disease_name": "Anal Cancer",
        "symptoms": ["anal bleeding", "pain during bowel movements", "anal mass", "itching"],
        "why": "Malignant cells develop in the anal canal tissue.",
        "medicines": ["Chemotherapy", "Radiation therapy", "Targeted therapy"],
        "home_remedies": ["Stool softeners", "Sitz baths"],
        "critical_conditions": ["Obstruction", "Perforation", "Sepsis"],
        "doctor_advice": "Seek immediate oncology evaluation.",
        "doctor_type": "Oncologist, Colorectal Surgeon"
    },
    "anaphylaxis": {
        "disease_name": "Anaphylaxis",
        "symptoms": ["difficulty breathing", "throat tightness", "rapid pulse", "dizziness", "loss of consciousness"],
        "why": "Severe allergic reaction causes rapid immune response affecting multiple body systems.",
        "medicines": ["Epinephrine injection", "Antihistamines", "Corticosteroids"],
        "home_remedies": ["Lay flat", "Elevate legs"],
        "critical_conditions": ["Respiratory collapse", "Cardiac arrest", "Shock"],
        "doctor_advice": "Call emergency services immediately. This is life-threatening.",
        "doctor_type": "Emergency Medicine, Allergist"
    },
    "angina": {
        "disease_name": "Angina",
        "symptoms": ["chest pain", "pressure in chest", "shortness of breath", "fatigue"],
        "why": "Heart doesn't receive enough oxygen due to blocked arteries.",
        "medicines": ["Nitrates", "Beta-blockers", "ACE inhibitors", "Aspirin"],
        "home_remedies": ["Rest", "Stress management", "Avoid exertion"],
        "critical_conditions": ["Heart attack", "Unstable angina"],
        "doctor_advice": "Seek medical care promptly. May need angiography.",
        "doctor_type": "Cardiologist"
    },
    "heart_attack": {
        "disease_name": "Heart Attack (Emergency)",
        "symptoms": ["chest pain", "pressure in chest", "shortness of breath", "nausea", "sweating", "pain in shoulder or jaw"],
        "why": "A blocked coronary artery reduces blood flow to heart muscle, causing an emergency heart attack.",
        "medicines": ["Aspirin only if already advised and safe", "Nitroglycerin only if prescribed", "Emergency cardiac medications in hospital"],
        "home_remedies": ["Sit upright and stay calm", "Do not drive yourself", "Call emergency services immediately"],
        "critical_conditions": ["Cardiac arrest", "Shock", "Severe breathing difficulty"],
        "doctor_advice": "Call emergency services now. This is a medical emergency. Hospital evaluation by emergency medicine and cardiology is required immediately.",
        "doctor_type": "Emergency Medicine, Cardiologist"
    },
    "angioedema": {
        "disease_name": "Angioedema",
        "symptoms": ["facial swelling", "throat swelling", "lip swelling", "difficulty breathing"],
        "why": "Deep tissue swelling occurs due to allergic reaction or hereditary causes.",
        "medicines": ["Antihistamines", "Corticosteroids", "Epinephrine if severe"],
        "home_remedies": ["Cold compresses", "Elevate head"],
        "critical_conditions": ["Airway obstruction", "Breathing failure"],
        "doctor_advice": "Seek emergency care if breathing is affected.",
        "doctor_type": "Emergency Medicine, Allergist"
    },
    "ankle_sprain": {
        "disease_name": "Ankle Sprain",
        "symptoms": ["ankle pain", "swelling", "bruising", "inability to walk"],
        "why": "Ligaments around ankle tear from sudden twisting motion.",
        "medicines": ["Pain relievers", "Anti-inflammatory medications"],
        "home_remedies": ["RICE protocol (Rest, Ice, Compression, Elevation)", "Ankle exercises"],
        "critical_conditions": ["Complete ligament rupture", "Fracture"],
        "doctor_advice": "Get X-rays to rule out fracture. May need physical therapy.",
        "doctor_type": "Orthopedist, Physical Therapist"
    },
    "ankle_avulsion_fracture": {
        "disease_name": "Ankle Avulsion Fracture",
        "symptoms": ["severe ankle pain", "swelling", "inability to bear weight", "bruising"],
        "why": "Bone fragment attached to ligament tears away from main bone.",
        "medicines": ["Pain management", "Anti-inflammatory drugs"],
        "home_remedies": ["Immobilization", "Ice", "Elevation"],
        "critical_conditions": ["Displacement", "Soft tissue damage", "Compartment syndrome"],
        "doctor_advice": "Requires orthopedic evaluation. May need surgery.",
        "doctor_type": "Orthopedic Surgeon"
    },
    "ankylosing_spondylitis": {
        "disease_name": "Ankylosing Spondylitis",
        "symptoms": ["lower back pain", "stiffness", "fatigue", "reduced mobility"],
        "why": "Inflammatory condition causes vertebrae to fuse over time.",
        "medicines": ["NSAIDs", "Biologic DMARDs", "TNF inhibitors"],
        "home_remedies": ["Regular exercise", "Good posture", "Heat therapy"],
        "critical_conditions": ["Severe spinal fusion", "Bowel problems"],
        "doctor_advice": "Work with rheumatologist for long-term management.",
        "doctor_type": "Rheumatologist"
    },
    "anorexia_nervosa": {
        "disease_name": "Anorexia Nervosa",
        "symptoms": ["extreme weight loss", "food restriction", "excessive exercise", "anxiety about weight"],
        "why": "Psychological disorder leading to severe calorie restriction.",
        "medicines": ["Antidepressants", "Anti-anxiety medications"],
        "home_remedies": ["Nutritional counseling", "Gradual food reintroduction"],
        "critical_conditions": ["Severe malnutrition", "Cardiac arrhythmias", "Organ failure"],
        "doctor_advice": "Requires psychiatric and medical intervention. Hospitalization may be needed.",
        "doctor_type": "Psychiatrist, Nutritionist, Internist"
    },
    "anxiety_disorders_children": {
        "disease_name": "Anxiety Disorders in Children and Young People",
        "symptoms": ["excessive worry", "restlessness", "irritability", "difficulty concentrating"],
        "why": "Brain chemistry imbalance causes excessive worry and fear responses.",
        "medicines": ["SSRIs", "Anxiety management medications"],
        "home_remedies": ["Cognitive behavioral therapy", "Relaxation techniques", "Physical activity"],
        "critical_conditions": ["School refusal", "Severe panic attacks"],
        "doctor_advice": "Seek child psychology evaluation and therapy.",
        "doctor_type": "Child Psychologist, Psychiatrist"
    },
    "appendicitis": {
        "disease_name": "Appendicitis",
        "symptoms": ["severe lower right abdominal pain", "nausea", "vomiting", "fever"],
        "why": "Appendix becomes inflamed, usually due to infection or obstruction.",
        "medicines": ["Antibiotics", "Pain management"],
        "home_remedies": ["NPO (nothing by mouth)", "Avoid eating"],
        "critical_conditions": ["Perforation", "Peritonitis", "Sepsis"],
        "doctor_advice": "Seek emergency care. Likely requires surgical removal.",
        "doctor_type": "Surgeon"
    },
    "arterial_thrombosis": {
        "disease_name": "Arterial Thrombosis",
        "symptoms": ["sudden severe pain", "cold limb", "pale skin", "muscle weakness"],
        "why": "Blood clot forms in artery blocking blood flow.",
        "medicines": ["Anticoagulants", "Thrombolytics", "Vasodilators"],
        "home_remedies": ["None - medical emergency"],
        "critical_conditions": ["Tissue death", "Limb loss", "Organ infarction"],
        "doctor_advice": "Call emergency services immediately.",
        "doctor_type": "Vascular Surgeon, Cardiologist"
    },
    "arthritis": {
        "disease_name": "Arthritis",
        "symptoms": ["joint pain", "stiffness", "swelling", "reduced range of motion"],
        "why": "Joint inflammation from degenerative or autoimmune causes.",
        "medicines": ["NSAIDs", "Corticosteroids", "Disease-modifying drugs"],
        "home_remedies": ["Joint rest", "Heat/cold therapy", "Gentle exercise"],
        "critical_conditions": ["Severe joint destruction", "Disability"],
        "doctor_advice": "Consult rheumatologist for proper management.",
        "doctor_type": "Rheumatologist, Orthopedist"
    },
    "asbestosis": {
        "disease_name": "Asbestosis",
        "symptoms": ["shortness of breath", "persistent cough", "chest pain", "fatigue"],
        "why": "Asbestos fibers damage lungs causing scarring and inflammation.",
        "medicines": ["Lung-protective medications", "Pain relievers"],
        "home_remedies": ["Avoid further exposure", "Pulmonary rehabilitation"],
        "critical_conditions": ["Lung cancer", "Mesothelioma", "Respiratory failure"],
        "doctor_advice": "Regular lung monitoring required. Avoid asbestos exposure.",
        "doctor_type": "Pulmonologist, Occupational Medicine"
    },
    "asthma": {
        "disease_name": "Asthma",
        "symptoms": ["wheezing", "shortness of breath", "chest tightness", "cough at night"],
        "why": "Airways become inflamed and narrow in response to triggers.",
        "medicines": ["Inhalers (bronchodilators)", "Corticosteroid inhalers", "Leukotriene inhibitors"],
        "home_remedies": ["Avoid triggers", "Breathing exercises", "Keep environment clean"],
        "critical_conditions": ["Severe asthma attack", "Status asthmaticus"],
        "doctor_advice": "Work with pulmonologist for action plan and medication management.",
        "doctor_type": "Pulmonologist, Allergist"
    },
    "ataxia": {
        "disease_name": "Ataxia",
        "symptoms": ["poor coordination", "unsteady gait", "slurred speech", "tremor"],
        "why": "Damage to cerebellum or nerve pathways affects coordination.",
        "medicines": ["Symptom management medications"],
        "home_remedies": ["Physical therapy", "Balance exercises"],
        "critical_conditions": ["Complete disability", "Falls and injuries"],
        "doctor_advice": "Requires neurologist evaluation and physical therapy.",
        "doctor_type": "Neurologist, Physical Therapist"
    },
    "atopic_eczema": {
        "disease_name": "Atopic Eczema",
        "symptoms": ["itchy skin", "dry skin", "rash", "skin irritation", "cracked skin"],
        "why": "Skin barrier dysfunction and immune system response cause inflammation.",
        "medicines": ["Topical corticosteroids", "Moisturizers", "Antihistamines"],
        "home_remedies": ["Skin hydration", "Avoid irritants", "Cool baths"],
        "critical_conditions": ["Severe infection", "Skin sepsis"],
        "doctor_advice": "Consult dermatologist for proper skin care regimen.",
        "doctor_type": "Dermatologist"
    },
    "atrial_fibrillation": {
        "disease_name": "Atrial Fibrillation",
        "symptoms": ["irregular heartbeat", "palpitations", "shortness of breath", "weakness"],
        "why": "Heart's upper chambers beat irregularly disrupting normal rhythm.",
        "medicines": ["Anticoagulants", "Rate control drugs", "Rhythm control drugs"],
        "home_remedies": ["Reduce caffeine", "Stress management", "Regular exercise"],
        "critical_conditions": ["Stroke", "Heart failure", "Cardiac shock"],
        "doctor_advice": "Requires cardiology care and possibly ablation therapy.",
        "doctor_type": "Cardiologist, Cardiac Electrophysiologist"
    },
    "attention_deficit_hyperactivity_disorder": {
        "disease_name": "Attention Deficit Hyperactivity Disorder (ADHD)",
        "symptoms": ["difficulty concentrating", "impulsivity", "hyperactivity", "forgetfulness"],
        "why": "Neurotransmitter imbalance affects attention and impulse control.",
        "medicines": ["Stimulants", "Non-stimulant medications"],
        "home_remedies": ["Behavioral therapy", "Structured routines", "Exercise"],
        "critical_conditions": ["Severe behavioral issues", "Academic failure"],
        "doctor_advice": "Get evaluation from psychiatrist and behavioral specialist.",
        "doctor_type": "Psychiatrist, Child Psychologist"
    },
    "autism": {
        "disease_name": "Autism",
        "symptoms": ["social communication difficulties", "repetitive behaviors", "sensory sensitivities"],
        "why": "Neurodevelopmental differences in brain structure and function.",
        "medicines": ["Symptom-specific medications for comorbidities"],
        "home_remedies": ["Behavioral therapy", "Social skills training", "Supportive environment"],
        "critical_conditions": ["Severe behavioral challenges", "Self-harm"],
        "doctor_advice": "Early diagnosis and intervention with specialists important.",
        "doctor_type": "Developmental Pediatrician, Child Psychologist"
    },
    "back_problems": {
        "disease_name": "Back Problems",
        "symptoms": ["back pain", "stiffness", "limited mobility", "radiating pain"],
        "why": "Muscle strain, disc herniation, or poor posture affects back.",
        "medicines": ["NSAIDs", "Muscle relaxants", "Pain relievers"],
        "home_remedies": ["Rest", "Back exercises", "Good posture", "Heat therapy"],
        "critical_conditions": ["Spinal cord compression", "Cauda equina syndrome"],
        "doctor_advice": "Consult physical therapist and orthopedist if pain persists.",
        "doctor_type": "Orthopedist, Physical Therapist"
    },
    "bacterial_vaginosis": {
        "disease_name": "Bacterial Vaginosis",
        "symptoms": ["vaginal discharge", "fishy odor", "vaginal itching", "burning during urination"],
        "why": "Imbalance of normal vaginal bacteria allows harmful bacteria overgrowth.",
        "medicines": ["Antibiotics (metronidazole, clindamycin)", "Vaginal gels"],
        "home_remedies": ["Avoid douching", "Maintain pH balance"],
        "critical_conditions": ["Pelvic inflammatory disease", "Pregnancy complications"],
        "doctor_advice": "Requires antibiotic treatment to prevent complications.",
        "doctor_type": "Gynecologist, Primary Care Physician"
    },
    "becker_muscular_dystrophy": {
        "disease_name": "Becker Muscular Dystrophy",
        "symptoms": ["muscle weakness", "waddling gait", "difficulty climbing stairs", "calf enlargement"],
        "why": "Genetic mutation causes progressive muscle fiber degeneration.",
        "medicines": ["Corticosteroids", "Supportive care medications"],
        "home_remedies": ["Physical therapy", "Assistive devices", "Genetic counseling"],
        "critical_conditions": ["Cardiomyopathy", "Respiratory failure"],
        "doctor_advice": "Requires genetics specialist and ongoing supportive care.",
        "doctor_type": "Neurologist, Genetic Counselor"
    },
    "benign_prostate_enlargement": {
        "disease_name": "Benign Prostate Enlargement",
        "symptoms": ["urinary urgency", "frequent urination", "weak urine stream", "nocturia"],
        "why": "Prostate gland enlarges with age affecting urine flow.",
        "medicines": ["Alpha-blockers", "5-alpha reductase inhibitors"],
        "home_remedies": ["Pelvic floor exercises", "Limit fluids before bed"],
        "critical_conditions": ["Urinary retention", "Bladder damage"],
        "doctor_advice": "Urology evaluation recommended for symptom management.",
        "doctor_type": "Urologist"
    },
    "bile_duct_cancer": {
        "disease_name": "Bile Duct Cancer (Cholangiocarcinoma)",
        "symptoms": ["jaundice", "abdominal pain", "weight loss", "pale stools"],
        "why": "Malignant cells develop in bile ducts blocking bile flow.",
        "medicines": ["Chemotherapy", "Radiation therapy", "Targeted therapy"],
        "home_remedies": ["Nutritious diet", "Rest"],
        "critical_conditions": ["Liver failure", "Bile duct obstruction"],
        "doctor_advice": "Requires immediate oncology and surgeon evaluation.",
        "doctor_type": "Oncologist, Hepatobiliary Surgeon"
    },
    "binge_eating_disorder": {
        "disease_name": "Binge Eating Disorder (BED)",
        "symptoms": ["uncontrolled eating episodes", "guilt after eating", "weight gain", "emotional eating"],
        "why": "Psychological factors cause episodes of excessive uncontrolled eating.",
        "medicines": ["Antidepressants", "Topiramate"],
        "home_remedies": ["Cognitive behavioral therapy", "Support groups"],
        "critical_conditions": ["Obesity", "Type 2 diabetes", "Heart disease"],
        "doctor_advice": "Requires psychiatric and nutritionist support.",
        "doctor_type": "Psychiatrist, Nutritionist"
    },
    "bipolar_disorder": {
        "disease_name": "Bipolar Disorder",
        "symptoms": ["mood swings", "depressive episodes", "manic episodes", "impulsive behavior"],
        "why": "Brain chemistry imbalance causes extreme mood fluctuations.",
        "medicines": ["Mood stabilizers", "Antipsychotics", "Antidepressants"],
        "home_remedies": ["Therapy", "Routine maintenance", "Sleep hygiene"],
        "critical_conditions": ["Suicidal ideation", "Severe mania"],
        "doctor_advice": "Requires psychiatry care and ongoing medication management.",
        "doctor_type": "Psychiatrist"
    },
    "bladder_cancer": {
        "disease_name": "Bladder Cancer",
        "symptoms": ["blood in urine", "urinary urgency", "dysuria", "abdominal pain"],
        "why": "Malignant cells develop in bladder lining.",
        "medicines": ["Chemotherapy", "Immunotherapy", "Targeted therapy"],
        "home_remedies": ["Increased fluids", "Dietary modifications"],
        "critical_conditions": ["Metastasis", "Bladder rupture"],
        "doctor_advice": "Requires urgent urology and oncology evaluation.",
        "doctor_type": "Urologist, Oncologist"
    },
    "blood_poisoning_sepsis": {
        "disease_name": "Blood Poisoning (Sepsis)",
        "symptoms": ["fever", "rapid heart rate", "difficulty breathing", "low blood pressure", "organ failure"],
        "why": "Systemic infection causes life-threatening inflammatory response.",
        "medicines": ["Antibiotics", "Vasopressors", "Supportive care"],
        "home_remedies": ["None - medical emergency"],
        "critical_conditions": ["Septic shock", "Multi-organ failure", "Death"],
        "doctor_advice": "Call emergency services immediately.",
        "doctor_type": "Emergency Medicine, Intensive Care"
    },
    "bone_cancer": {
        "disease_name": "Bone Cancer",
        "symptoms": ["bone pain", "swelling", "reduced mobility", "fractures"],
        "why": "Malignant cells develop in bone tissue.",
        "medicines": ["Chemotherapy", "Radiation", "Surgery"],
        "home_remedies": ["Pain management", "Physical therapy"],
        "critical_conditions": ["Metastasis", "Pathological fractures"],
        "doctor_advice": "Requires immediate oncology and orthopedic evaluation.",
        "doctor_type": "Oncologist, Orthopedic Surgeon"
    },
    "bowel_cancer": {
        "disease_name": "Bowel Cancer",
        "symptoms": ["blood in stool", "change in bowel habits", "abdominal pain", "weight loss"],
        "why": "Malignant cells develop in colon or rectum.",
        "medicines": ["Chemotherapy", "Immunotherapy", "Targeted therapy"],
        "home_remedies": ["Dietary modifications", "Exercise"],
        "critical_conditions": ["Obstruction", "Perforation", "Metastasis"],
        "doctor_advice": "Requires immediate colorectal surgeon and oncologist evaluation.",
        "doctor_type": "Colorectal Surgeon, Oncologist"
    },
    "bowel_incontinence": {
        "disease_name": "Bowel Incontinence",
        "symptoms": ["uncontrolled stool passage", "soiling", "urgency", "embarrassment"],
        "why": "Loss of control over bowel sphincters from various causes.",
        "medicines": ["Antidiarrheal medications", "Stool softeners"],
        "home_remedies": ["Dietary changes", "Pelvic floor exercises", "Scheduled toileting"],
        "critical_conditions": ["Skin breakdown", "Infection"],
        "doctor_advice": "Consult gastroenterologist and colorectal surgeon.",
        "doctor_type": "Gastroenterologist, Colorectal Surgeon"
    },
    "bowel_polyps": {
        "disease_name": "Bowel Polyps",
        "symptoms": ["usually asymptomatic", "blood in stool", "constipation"],
        "why": "Abnormal tissue growths in bowel lining may become cancerous.",
        "medicines": ["Preventive medications"],
        "home_remedies": ["High fiber diet", "Regular exercise"],
        "critical_conditions": ["Malignant transformation"],
        "doctor_advice": "Require endoscopic removal and regular screening.",
        "doctor_type": "Gastroenterologist, Colorectal Surgeon"
    },
    "brain_tumours": {
        "disease_name": "Brain Tumours",
        "symptoms": ["headache", "vision changes", "balance problems", "seizures", "cognitive changes"],
        "why": "Abnormal cell growth in brain tissue disrupts normal function.",
        "medicines": ["Chemotherapy", "Radiation", "Targeted therapy"],
        "home_remedies": ["None - requires medical intervention"],
        "critical_conditions": ["Brain herniation", "Stroke", "Death"],
        "doctor_advice": "Requires immediate neurosurgery and oncology evaluation.",
        "doctor_type": "Neurosurgeon, Neuro-Oncologist"
    },
    "breast_cancer_women": {
        "disease_name": "Breast Cancer in Women",
        "symptoms": ["breast lump", "nipple discharge", "breast pain", "skin changes"],
        "why": "Malignant cells develop in breast tissue.",
        "medicines": ["Chemotherapy", "Hormone therapy", "Immunotherapy", "Targeted therapy"],
        "home_remedies": ["Support groups", "Nutritious diet"],
        "critical_conditions": ["Metastasis", "Complications from treatment"],
        "doctor_advice": "Requires immediate oncology evaluation.",
        "doctor_type": "Breast Surgeon, Oncologist"
    },
    "breast_cancer_men": {
        "disease_name": "Breast Cancer in Men",
        "symptoms": ["breast lump", "nipple discharge", "breast pain", "nipple inversion"],
        "why": "Malignant cells develop in breast tissue in men.",
        "medicines": ["Chemotherapy", "Hormone therapy", "Immunotherapy"],
        "home_remedies": ["Support groups", "Nutritious diet"],
        "critical_conditions": ["Metastasis", "Spread to lymph nodes"],
        "doctor_advice": "Requires immediate oncology evaluation.",
        "doctor_type": "Breast Surgeon, Oncologist"
    },
    "bronchiectasis": {
        "disease_name": "Bronchiectasis",
        "symptoms": ["persistent cough", "copious sputum", "hemoptysis", "recurrent infections"],
        "why": "Permanent airway dilation causes chronic infection and inflammation.",
        "medicines": ["Antibiotics", "Bronchodilators", "Mucolytics"],
        "home_remedies": ["Chest physiotherapy", "Airway clearance techniques"],
        "critical_conditions": ["Massive hemoptysis", "Respiratory failure"],
        "doctor_advice": "Requires pulmonologist care and regular monitoring.",
        "doctor_type": "Pulmonologist"
    },
    "bronchitis": {
        "disease_name": "Bronchitis",
        "symptoms": ["persistent cough", "mucus production", "fatigue", "shortness of breath"],
        "why": "Inflammation of bronchial tubes from infection or irritation.",
        "medicines": ["Cough suppressants", "Bronchodilators", "Antibiotics if bacterial"],
        "home_remedies": ["Rest", "Steam inhalation", "Fluids", "Honey"],
        "critical_conditions": ["Pneumonia", "Respiratory failure"],
        "doctor_advice": "Rest and monitor. See doctor if symptoms worsen.",
        "doctor_type": "Pulmonologist, General Practitioner"
    },
    "bulimia_nervosa": {
        "disease_name": "Bulimia Nervosa",
        "symptoms": ["binge eating followed by purging", "weight fluctuation", "dental erosion", "throat irritation"],
        "why": "Psychological disorder causing compulsive eating followed by purging.",
        "medicines": ["Antidepressants", "Anti-anxiety medications"],
        "home_remedies": ["Cognitive behavioral therapy", "Support groups"],
        "critical_conditions": ["Electrolyte imbalance", "Cardiac arrhythmias"],
        "doctor_advice": "Requires psychiatric and medical intervention.",
        "doctor_type": "Psychiatrist, Internist"
    },
    "bunion": {
        "disease_name": "Bunion (Hallux Valgus)",
        "symptoms": ["big toe deviation", "toe pain", "bunion bump", "difficulty walking"],
        "why": "Big toe joint misalignment causes pressure and inflammation.",
        "medicines": ["Pain relievers", "Anti-inflammatory medications"],
        "home_remedies": ["Proper footwear", "Toe exercises", "Ice therapy"],
        "critical_conditions": ["Severe deformity", "Mobility loss"],
        "doctor_advice": "Consult podiatrist. May need surgical correction.",
        "doctor_type": "Podiatrist, Orthopedist"
    },
    "cardiac_arrest": {
        "disease_name": "Cardiac Arrest",
        "symptoms": ["sudden loss of consciousness", "no pulse", "no breathing"],
        "why": "Heart stops beating effectively cutting off blood supply.",
        "medicines": ["Emergency epinephrine", "Supportive medications"],
        "home_remedies": ["None - CPR required immediately"],
        "critical_conditions": ["Cardiac arrest itself", "Brain damage"],
        "doctor_advice": "Call 911 immediately. CPR needed.",
        "doctor_type": "Emergency Medicine, Cardiologist"
    },
    "cardiovascular_disease": {
        "disease_name": "Cardiovascular Disease",
        "symptoms": ["chest pain", "shortness of breath", "fatigue", "palpitations"],
        "why": "Heart and blood vessel disease reduces blood flow.",
        "medicines": ["Statins", "Beta-blockers", "ACE inhibitors", "Antiplatelet drugs"],
        "home_remedies": ["Heart-healthy diet", "Regular exercise", "Stress reduction"],
        "critical_conditions": ["Heart attack", "Stroke", "Heart failure"],
        "doctor_advice": "Requires cardiology care and lifestyle modifications.",
        "doctor_type": "Cardiologist"
    },
    "carpal_tunnel_syndrome": {
        "disease_name": "Carpal Tunnel Syndrome",
        "symptoms": ["hand numbness", "tingling fingers", "hand pain", "weak grip"],
        "why": "Median nerve compressed in wrist causing pain and numbness.",
        "medicines": ["Anti-inflammatory medications", "Corticosteroid injections"],
        "home_remedies": ["Wrist splinting", "Rest", "Ice therapy", "Stretching"],
        "critical_conditions": ["Permanent nerve damage", "Muscle atrophy"],
        "doctor_advice": "Consult orthopedist. May need surgery.",
        "doctor_type": "Orthopedist, Hand Surgeon"
    },
    "catarrh": {
        "disease_name": "Catarrh",
        "symptoms": ["postnasal drip", "throat irritation", "nasal congestion", "persistent cough"],
        "why": "Excessive mucus production in nasal passages and throat.",
        "medicines": ["Decongestants", "Antihistamines", "Saline rinses"],
        "home_remedies": ["Nasal rinse", "Steam inhalation", "Honey"],
        "critical_conditions": ["Sinusitis", "Otitis media"],
        "doctor_advice": "See ENT if symptoms persist beyond 2 weeks.",
        "doctor_type": "ENT Specialist"
    },
    "cellulitis": {
        "disease_name": "Cellulitis",
        "symptoms": ["skin redness", "swelling", "warmth", "pain", "fever"],
        "why": "Bacterial infection spreads through skin and tissue causing inflammation.",
        "medicines": ["Oral or IV antibiotics"],
        "home_remedies": ["Elevation", "Ice", "Rest"],
        "critical_conditions": ["Sepsis", "Abscess formation", "Necrotizing fasciitis"],
        "doctor_advice": "Seek immediate medical care. Requires antibiotics.",
        "doctor_type": "General Practitioner, Infectious Disease"
    },
    "cerebral_palsy": {
        "disease_name": "Cerebral Palsy",
        "symptoms": ["muscle stiffness", "poor coordination", "mobility limitations", "speech difficulties"],
        "why": "Brain injury during development affects motor control.",
        "medicines": ["Muscle relaxants", "Spasticity medications"],
        "home_remedies": ["Physical therapy", "Occupational therapy", "Assistive devices"],
        "critical_conditions": ["Severe disability", "Seizures"],
        "doctor_advice": "Requires multidisciplinary rehabilitation approach.",
        "doctor_type": "Pediatric Neurologist, Physical Therapist"
    },
    "cervical_cancer": {
        "disease_name": "Cervical Cancer",
        "symptoms": ["vaginal bleeding", "pelvic pain", "abnormal discharge", "dysuria"],
        "why": "Malignant cells develop in cervix.",
        "medicines": ["Chemotherapy", "Radiation", "Surgery"],
        "home_remedies": ["Nutritious diet", "Supportive care"],
        "critical_conditions": ["Metastasis", "Bleeding"],
        "doctor_advice": "Requires immediate gynecologic oncology evaluation.",
        "doctor_type": "Gynecologic Oncologist"
    },
    "cervical_spondylosis": {
        "disease_name": "Cervical Spondylosis",
        "symptoms": ["neck pain", "stiffness", "upper limb pain", "headache"],
        "why": "Cervical spine degenerates causing nerve compression.",
        "medicines": ["NSAIDs", "Muscle relaxants", "Corticosteroids"],
        "home_remedies": ["Neck exercises", "Proper posture", "Heat therapy"],
        "critical_conditions": ["Myelopathy", "Spinal cord compression"],
        "doctor_advice": "Consult neurologist or orthopedist for management.",
        "doctor_type": "Neurologist, Orthopedist"
    },
    "chest_and_rib_injury": {
        "disease_name": "Chest and Rib Injury",
        "symptoms": ["chest pain", "swelling", "difficulty breathing", "bruising"],
        "why": "Trauma causes rib fractures and soft tissue damage.",
        "medicines": ["Pain relievers", "Anti-inflammatory medications"],
        "home_remedies": ["Rest", "Ice", "Breathing exercises"],
        "critical_conditions": ["Pneumothorax", "Hemothorax", "Flail chest"],
        "doctor_advice": "Get chest X-ray to rule out serious injury.",
        "doctor_type": "Orthopedist, Emergency Medicine"
    },
    "chest_infection": {
        "disease_name": "Chest Infection",
        "symptoms": ["cough", "fever", "chest pain", "shortness of breath"],
        "why": "Viral or bacterial infection affects lower respiratory tract.",
        "medicines": ["Antibiotics if bacterial", "Cough suppressants", "Pain relievers"],
        "home_remedies": ["Rest", "Steam inhalation", "Fluids"],
        "critical_conditions": ["Pneumonia", "Sepsis"],
        "doctor_advice": "See doctor if symptoms persist beyond 1 week.",
        "doctor_type": "Pulmonologist, General Practitioner"
    },
    "chickenpox": {
        "disease_name": "Chickenpox",
        "symptoms": ["fever", "rash", "itching", "malaise"],
        "why": "Varicella zoster virus causes characteristic blistering rash.",
        "medicines": ["Acyclovir if prescribed", "Pain relievers"],
        "home_remedies": ["Oatmeal baths", "Cool compresses", "Calamine lotion"],
        "critical_conditions": ["Secondary infection", "Pneumonia", "Encephalitis"],
        "doctor_advice": "Rest at home. See doctor if complications develop.",
        "doctor_type": "General Practitioner"
    },
    "chilblains": {
        "disease_name": "Chilblains",
        "symptoms": ["itching and burning pain", "redness", "swelling", "blistering"],
        "why": "Cold exposure followed by rapid rewarming damages skin.",
        "medicines": ["Pain relievers", "Topical treatments"],
        "home_remedies": ["Gradual warming", "Avoid scratching", "Moisturizers"],
        "critical_conditions": ["Infection", "Tissue necrosis"],
        "doctor_advice": "Prevent further cold exposure.",
        "doctor_type": "Dermatologist"
    },
    "chlamydia": {
        "disease_name": "Chlamydia",
        "symptoms": ["urethritis", "cervicitis", "discharge", "dysuria", "pelvic pain"],
        "why": "Bacterial infection of genital tract.",
        "medicines": ["Antibiotics (doxycycline, azithromycin)"],
        "home_remedies": ["Avoid sexual contact", "Pelvic rest"],
        "critical_conditions": ["Pelvic inflammatory disease", "Infertility"],
        "doctor_advice": "Requires antibiotic treatment and partner notification.",
        "doctor_type": "Gynecologist, Urology, STI Specialist"
    },
    "chronic_fatigue_syndrome": {
        "disease_name": "Chronic Fatigue Syndrome",
        "symptoms": ["severe fatigue", "post-exertional malaise", "cognitive dysfunction", "pain"],
        "why": "Prolonged viral infection or immune dysfunction causes debilitating fatigue.",
        "medicines": ["Symptom management medications"],
        "home_remedies": ["Gradual exercise", "Sleep hygiene", "Pacing"],
        "critical_conditions": ["Complete disability"],
        "doctor_advice": "Requires specialist care and multidisciplinary support.",
        "doctor_type": "Internal Medicine, Infectious Disease"
    },
    "chronic_kidney_disease": {
        "disease_name": "Chronic Kidney Disease",
        "symptoms": ["fatigue", "high blood pressure", "edema", "urinary changes"],
        "why": "Gradual loss of kidney function from various causes.",
        "medicines": ["ACE inhibitors", "Blood pressure control", "Diuretics"],
        "home_remedies": ["Low sodium diet", "Fluid management", "Regular monitoring"],
        "critical_conditions": ["Kidney failure", "Uremia"],
        "doctor_advice": "Requires nephrologist care and regular monitoring.",
        "doctor_type": "Nephrologist"
    },
    "chronic_lymphocytic_leukaemia": {
        "disease_name": "Chronic Lymphocytic Leukaemia (CLL)",
        "symptoms": ["fatigue", "enlarged lymph nodes", "splenomegaly", "frequent infections"],
        "why": "Slow growth of abnormal lymphoid cells.",
        "medicines": ["Chemotherapy", "Targeted therapy", "Watch and wait"],
        "home_remedies": ["Infection prevention", "Nutrition"],
        "critical_conditions": ["Richter transformation", "Infections"],
        "doctor_advice": "Requires hematology/oncology care and monitoring.",
        "doctor_type": "Hematologist, Oncologist"
    },
    "chronic_myeloid_leukaemia": {
        "disease_name": "Chronic Myeloid Leukaemia (CML)",
        "symptoms": ["fatigue", "abdominal swelling", "night sweats", "bone pain"],
        "why": "BCR-ABL fusion gene causes excessive myeloid cell production.",
        "medicines": ["Tyrosine kinase inhibitors", "Chemotherapy"],
        "home_remedies": ["Regular monitoring", "Supportive care"],
        "critical_conditions": ["Blast crisis", "Organ failure"],
        "doctor_advice": "Requires targeted therapy and close monitoring.",
        "doctor_type": "Hematologist, Oncologist"
    },
    "chronic_obstructive_pulmonary_disease": {
        "disease_name": "Chronic Obstructive Pulmonary Disease (COPD)",
        "symptoms": ["shortness of breath", "chronic cough", "sputum production", "wheezing"],
        "why": "Smoking or air pollution damages airways causing airflow limitation.",
        "medicines": ["Inhalers", "Bronchodilators", "Corticosteroids"],
        "home_remedies": ["Smoking cessation", "Pulmonary rehabilitation", "Oxygen therapy"],
        "critical_conditions": ["Acute exacerbation", "Respiratory failure"],
        "doctor_advice": "Requires pulmonologist care and smoking cessation.",
        "doctor_type": "Pulmonologist"
    },
    "chronic_pain": {
        "disease_name": "Chronic Pain",
        "symptoms": ["persistent pain lasting >3 months", "disability", "emotional distress"],
        "why": "Various causes lead to ongoing pain beyond normal healing.",
        "medicines": ["Analgesics", "Neuropathic pain medications", "Adjuvants"],
        "home_remedies": ["Physical therapy", "Psychological therapy", "Exercise"],
        "critical_conditions": ["Opioid dependence", "Suicide risk"],
        "doctor_advice": "Requires multidisciplinary pain management approach.",
        "doctor_type": "Pain Medicine Specialist"
    },
    "chronic_pancreatitis": {
        "disease_name": "Chronic Pancreatitis",
        "symptoms": ["abdominal pain", "malabsorption", "diabetes", "steatorrhea"],
        "why": "Repeated pancreatic inflammation leads to irreversible damage.",
        "medicines": ["Pancreatic enzymes", "Pain management", "Diabetes medications"],
        "home_remedies": ["Abstain from alcohol", "Low fat diet"],
        "critical_conditions": ["Pancreatic cancer", "Pancreatic insufficiency"],
        "doctor_advice": "Requires gastroenterology care and lifestyle changes.",
        "doctor_type": "Gastroenterologist"
    },
    "cirrhosis": {
        "disease_name": "Cirrhosis",
        "symptoms": ["jaundice", "ascites", "edema", "hepatic encephalopathy"],
        "why": "Liver scarring leads to loss of liver function.",
        "medicines": ["Diuretics", "Beta-blockers", "Liver protective drugs"],
        "home_remedies": ["Alcohol abstinence", "Low sodium diet"],
        "critical_conditions": ["Variceal bleeding", "Hepatic coma", "Liver failure"],
        "doctor_advice": "Requires hepatologist care and may need transplant.",
        "doctor_type": "Hepatologist"
    },
    "clavicle_fracture": {
        "disease_name": "Clavicle (Collar Bone) Fracture",
        "symptoms": ["shoulder pain", "deformity", "swelling", "limitation of arm movement"],
        "why": "Direct blow or fall fractures the clavicle.",
        "medicines": ["Pain relievers", "Anti-inflammatory medications"],
        "home_remedies": ["Sling immobilization", "Ice", "Rest"],
        "critical_conditions": ["Neurovascular injury", "Nonunion"],
        "doctor_advice": "Most heal with conservative treatment. Surgery if severely displaced.",
        "doctor_type": "Orthopedist"
    },
    "clostridium_difficile": {
        "disease_name": "Clostridium Difficile",
        "symptoms": ["severe diarrhea", "abdominal pain", "fever", "leukocytosis"],
        "why": "Bacterial toxins damage colon lining after antibiotic use.",
        "medicines": ["Metronidazole", "Vancomycin", "Fidaxomicin"],
        "home_remedies": ["Fluid replacement", "Infection control"],
        "critical_conditions": ["Fulminant colitis", "Toxic megacolon"],
        "doctor_advice": "Requires antibiotic treatment and isolation precautions.",
        "doctor_type": "Gastroenterologist, Infectious Disease"
    },
    "coeliac_disease": {
        "disease_name": "Coeliac Disease",
        "symptoms": ["diarrhea", "abdominal pain", "bloating", "malabsorption"],
        "why": "Gluten triggers immune attack on small intestine.",
        "medicines": ["No specific medicine - gluten-free diet is cure"],
        "home_remedies": ["Gluten-free diet", "Nutritional supplementation"],
        "critical_conditions": ["Intestinal lymphoma", "Osteoporosis"],
        "doctor_advice": "Lifelong gluten avoidance required.",
        "doctor_type": "Gastroenterologist"
    },
    "cold_sore": {
        "disease_name": "Cold Sore",
        "symptoms": ["lip blistering", "pain", "itching", "viral shedding"],
        "why": "Herpes simplex virus reactivation causes painful blisters.",
        "medicines": ["Acyclovir", "Valacyclovir", "Topical treatments"],
        "home_remedies": ["Avoid triggers", "Topical ice", "Lip protection"],
        "critical_conditions": ["Herpetic whitlow", "Ocular herpes"],
        "doctor_advice": "Use antivirals to shorten duration.",
        "doctor_type": "Dermatologist"
    },
    "coma": {
        "disease_name": "Coma",
        "symptoms": ["unresponsiveness", "lack of sleep-wake cycle", "absent purposeful movement"],
        "why": "Severe brain injury or metabolic failure causes loss of consciousness.",
        "medicines": ["Supportive medications", "Brain protective agents"],
        "home_remedies": ["None - ICU care required"],
        "critical_conditions": ["Coma itself", "Brain death"],
        "doctor_advice": "Requires intensive medical care and neurologic evaluation.",
        "doctor_type": "Neurologist, Critical Care"
    },
    "common_cold": {
        "disease_name": "Common Cold",
        "symptoms": ["runny nose", "cough", "sore throat", "sneezing"],
        "why": "Viral infection of upper respiratory tract.",
        "medicines": ["Cough syrup", "Lozenges", "Pain relievers"],
        "home_remedies": ["Rest", "Warm fluids", "Honey", "Steam inhalation"],
        "critical_conditions": ["Secondary bacterial infection", "Pneumonia"],
        "doctor_advice": "Rest at home. Antibiotics don't help viral colds.",
        "doctor_type": "General Practitioner"
    },
    "complications_type_1_diabetes": {
        "disease_name": "Complications of Type 1 Diabetes",
        "symptoms": ["high blood sugar", "ketoacidosis", "long-term complications"],
        "why": "Uncontrolled blood sugar leads to acute and chronic complications.",
        "medicines": ["Insulin", "Complication-specific medications"],
        "home_remedies": ["Blood sugar monitoring", "Diet management", "Exercise"],
        "critical_conditions": ["DKA", "HHS", "Hypoglycemia"],
        "doctor_advice": "Requires endocrinology care and tight glucose control.",
        "doctor_type": "Endocrinologist"
    },
    "concussion": {
        "disease_name": "Concussion",
        "symptoms": ["headache", "confusion", "dizziness", "memory problems"],
        "why": "Head trauma causes temporary brain dysfunction.",
        "medicines": ["Pain relievers", "Symptomatic treatment"],
        "home_remedies": ["Physical and mental rest", "Gradual return to activity"],
        "critical_conditions": ["Intracranial hemorrhage", "Second impact syndrome"],
        "doctor_advice": "Avoid further head trauma. Follow concussion protocol.",
        "doctor_type": "Neurologist, Sports Medicine"
    },
    "congenital_heart_disease": {
        "disease_name": "Congenital Heart Disease",
        "symptoms": ["cyanosis", "shortness of breath", "feeding difficulties", "poor growth"],
        "why": "Heart structure abnormalities present at birth.",
        "medicines": ["Cardiac medications", "Prostaglandin inhibitors"],
        "home_remedies": ["Dietary modifications", "Activity restriction"],
        "critical_conditions": ["Heart failure", "Arrhythmias"],
        "doctor_advice": "May require surgical repair. Requires cardiology management.",
        "doctor_type": "Pediatric Cardiologist, Cardiac Surgeon"
    },
    "conjunctivitis": {
        "disease_name": "Conjunctivitis",
        "symptoms": ["red eyes", "discharge", "itching", "tearing"],
        "why": "Inflammation of eye membrane from infection or allergy.",
        "medicines": ["Eye drops", "Antibiotics if bacterial", "Antihistamines if allergic"],
        "home_remedies": ["Warm compresses", "Eye hygiene", "Avoid contact lenses"],
        "critical_conditions": ["Corneal involvement", "Vision loss"],
        "doctor_advice": "See ophthalmologist if vision affected.",
        "doctor_type": "Ophthalmologist"
    },
    "constipation": {
        "disease_name": "Constipation",
        "symptoms": ["infrequent bowel movements", "hard stools", "straining", "abdominal discomfort"],
        "why": "Slow colon movement or dehydration leads to hard stools.",
        "medicines": ["Stool softeners", "Laxatives", "Osmotic agents"],
        "home_remedies": ["Increase fiber", "Drink fluids", "Regular exercise"],
        "critical_conditions": ["Bowel obstruction", "Toxic megacolon"],
        "doctor_advice": "Rule out underlying causes. Try dietary changes first.",
        "doctor_type": "Gastroenterologist"
    },
    "coronary_heart_disease": {
        "disease_name": "Coronary Heart Disease",
        "symptoms": ["chest pain", "angina", "shortness of breath", "fatigue"],
        "why": "Atherosclerosis narrows coronary arteries reducing blood flow.",
        "medicines": ["Statins", "Antiplatelet drugs", "Beta-blockers", "Nitrates"],
        "home_remedies": ["Heart-healthy diet", "Exercise", "Stress management"],
        "critical_conditions": ["Myocardial infarction", "Cardiogenic shock"],
        "doctor_advice": "Requires cardiology care and angiography.",
        "doctor_type": "Cardiologist"
    },
    "coronavirus_covid_19": {
        "disease_name": "Coronavirus (COVID-19)",
        "symptoms": ["fever", "cough", "fatigue", "loss of taste/smell"],
        "why": "SARS-CoV-2 virus causes respiratory and systemic infection.",
        "medicines": ["Antivirals", "Supportive care", "Vaccines"],
        "home_remedies": ["Isolation", "Rest", "Fluids"],
        "critical_conditions": ["Severe pneumonia", "ARDS", "Sepsis"],
        "doctor_advice": "Get tested. Seek medical care if severe symptoms.",
        "doctor_type": "Pulmonologist, Infectious Disease"
    },
    "costochondritis": {
        "disease_name": "Costochondritis",
        "symptoms": ["chest pain", "tenderness", "worse with movement", "inflammation"],
        "why": "Inflammation at cartilage where ribs join sternum.",
        "medicines": ["NSAIDs", "Local corticosteroid injections"],
        "home_remedies": ["Rest", "Ice", "Stretching", "Activity modification"],
        "critical_conditions": ["Chronic pain syndrome"],
        "doctor_advice": "Rule out cardiac cause. Most improve with conservative care.",
        "doctor_type": "General Practitioner, Orthopedist"
    },
    "crohns_disease": {
        "disease_name": "Crohn's Disease",
        "symptoms": ["diarrhea", "abdominal pain", "weight loss", "rectal bleeding"],
        "why": "Autoimmune inflammation affects entire GI tract.",
        "medicines": ["Aminosalicylates", "Corticosteroids", "Immunosuppressants", "Biologics"],
        "home_remedies": ["Specific carbohydrate diet", "Stress management"],
        "critical_conditions": ["Perforation", "Sepsis", "Toxic megacolon"],
        "doctor_advice": "Requires gastroenterology care and medication management.",
        "doctor_type": "Gastroenterologist"
    },
    "croup": {
        "disease_name": "Croup",
        "symptoms": ["barking cough", "stridor", "hoarseness", "respiratory distress"],
        "why": "Viral inflammation of larynx and trachea.",
        "medicines": ["Dexamethasone", "Epinephrine if severe", "Cough suppressants"],
        "home_remedies": ["Steam inhalation", "Cool air", "Fluids"],
        "critical_conditions": ["Airway obstruction", "Epiglottitis"],
        "doctor_advice": "Seek medical care if breathing severely affected.",
        "doctor_type": "Pediatrician, Emergency Medicine"
    },
    "cystic_fibrosis": {
        "disease_name": "Cystic Fibrosis",
        "symptoms": ["chronic cough", "pancreatic insufficiency", "failure to thrive", "salt losses"],
        "why": "CFTR gene defect causes thick mucus blocking lungs and ducts.",
        "medicines": ["Pancreatic enzymes", "Pulmonary medications", "Antibiotics"],
        "home_remedies": ["Chest physiotherapy", "Nutritional support"],
        "critical_conditions": ["Respiratory failure", "Pancreatic cancer"],
        "doctor_advice": "Requires specialized CF center care and lifelong management.",
        "doctor_type": "Pulmonologist specializing in CF"
    },
    "cystitis": {
        "disease_name": "Cystitis",
        "symptoms": ["dysuria", "frequency", "urgency", "suprapubic pain"],
        "why": "Bacterial infection inflames bladder lining.",
        "medicines": ["Antibiotics", "Pain relievers"],
        "home_remedies": ["Increase fluids", "Cranberry juice", "Urinalysis"],
        "critical_conditions": ["Pyelonephritis", "Sepsis"],
        "doctor_advice": "See doctor for urine culture and antibiotics.",
        "doctor_type": "Urologist, General Practitioner"
    },
    "deafblindness": {
        "disease_name": "Deafblindness",
        "symptoms": ["hearing loss", "vision loss", "communication difficulty"],
        "why": "Combined deaf and blind conditions significantly impact communication.",
        "medicines": ["Symptom management"],
        "home_remedies": ["Assistive devices", "Specialized training"],
        "critical_conditions": ["Total isolation", "Behavioral issues"],
        "doctor_advice": "Requires specialized rehabilitation and communication training.",
        "doctor_type": "Audiologist, Ophthalmologist"
    },
    "deep_vein_thrombosis": {
        "disease_name": "Deep Vein Thrombosis",
        "symptoms": ["leg swelling", "pain", "warmth", "skin discoloration"],
        "why": "Blood clot forms in deep leg veins blocking blood flow.",
        "medicines": ["Anticoagulants", "Thrombolytics if urgent"],
        "home_remedies": ["Leg elevation", "Compression stockings"],
        "critical_conditions": ["Pulmonary embolism", "Post-thrombotic syndrome"],
        "doctor_advice": "Seek immediate medical care. Requires anticoagulation.",
        "doctor_type": "Vascular Surgeon, Cardiologist"
    },
    "degenerative_cervical_myelopathy": {
        "disease_name": "Degenerative Cervical Myelopathy",
        "symptoms": ["neck pain", "hand numbness", "balance problems", "weakness"],
        "why": "Cervical spine degeneration compresses spinal cord.",
        "medicines": ["NSAIDs", "Corticosteroids"],
        "home_remedies": ["Neck exercises", "Physical therapy"],
        "critical_conditions": ["Spinal cord injury", "Paralysis"],
        "doctor_advice": "May require surgical decompression.",
        "doctor_type": "Neurosurgeon"
    },
    "dehydration": {
        "disease_name": "Dehydration",
        "symptoms": ["thirst", "dry mouth", "fatigue", "dizziness"],
        "why": "Loss of body fluids exceeds intake.",
        "medicines": ["Oral rehydration salts", "IV fluids if severe"],
        "home_remedies": ["Drink water", "Electrolyte solutions", "Rest"],
        "critical_conditions": ["Severe hypovolemia", "Shock"],
        "doctor_advice": "Drink fluids gradually. Seek medical care if severe.",
        "doctor_type": "General Practitioner, Emergency Medicine"
    },
    "delirium": {
        "disease_name": "Delirium",
        "symptoms": ["confusion", "hallucinations", "agitation", "attention problems"],
        "why": "Acute medical illness or medication causes temporary mental status changes.",
        "medicines": ["Treat underlying cause", "Symptom management"],
        "home_remedies": ["Reorientation", "Supportive care"],
        "critical_conditions": ["Aspiration", "Self-injury"],
        "doctor_advice": "Identify and treat underlying cause urgently.",
        "doctor_type": "Psychiatrist, Internist"
    },
    "dementia": {
        "disease_name": "Dementia",
        "symptoms": ["memory loss", "cognitive decline", "behavioral changes"],
        "why": "Progressive brain cell death causes cognitive decline.",
        "medicines": ["Cholinesterase inhibitors", "Memantine"],
        "home_remedies": ["Cognitive stimulation", "Support system"],
        "critical_conditions": ["Severe dementia", "Inability to care for self"],
        "doctor_advice": "Requires neurologist care and family support planning.",
        "doctor_type": "Neurologist, Geriatrician"
    },
    "dementia_with_lewy_bodies": {
        "disease_name": "Dementia with Lewy Bodies",
        "symptoms": ["cognitive decline", "visual hallucinations", "Parkinsonism", "fluctuations"],
        "why": "Lewy body deposits damage brain cells.",
        "medicines": ["Cholinesterase inhibitors", "Dopaminergic agents"],
        "home_remedies": ["Cognitive exercises", "Support groups"],
        "critical_conditions": ["Falls", "Aspiration"],
        "doctor_advice": "Requires neurologist care and specialized management.",
        "doctor_type": "Neurologist"
    },
    "dental_abscess": {
        "disease_name": "Dental Abscess",
        "symptoms": ["tooth pain", "swelling", "fever", "difficulty chewing"],
        "why": "Bacterial infection develops inside tooth or gum.",
        "medicines": ["Antibiotics", "Pain relievers"],
        "home_remedies": ["Warm salt rinse", "Clove oil"],
        "critical_conditions": ["Sepsis", "Airway obstruction"],
        "doctor_advice": "Requires dental evaluation and possibly root canal or extraction.",
        "doctor_type": "Dentist, Oral Surgeon"
    },
    "depression": {
        "disease_name": "Depression",
        "symptoms": ["persistent sadness", "loss of interest", "fatigue", "suicidal thoughts"],
        "why": "Brain chemistry imbalance affects mood and motivation.",
        "medicines": ["SSRIs", "SNRIs", "Other antidepressants"],
        "home_remedies": ["Therapy", "Exercise", "Social support"],
        "critical_conditions": ["Suicide risk", "Severe functional impairment"],
        "doctor_advice": "Seek psychiatric and psychological support.",
        "doctor_type": "Psychiatrist, Psychologist"
    },
    "dermatitis_herpetiformis": {
        "disease_name": "Dermatitis Herpetiformis",
        "symptoms": ["intensely itchy skin lesions", "grouped blisters", "burning"],
        "why": "Gluten-related autoimmune skin condition.",
        "medicines": ["Dapsone", "Sulfasalazine"],
        "home_remedies": ["Gluten-free diet", "Skin care"],
        "critical_conditions": ["Secondary infection", "G6PD deficiency complications"],
        "doctor_advice": "Gluten-free diet is essential treatment.",
        "doctor_type": "Dermatologist, Gastroenterologist"
    },
    "diabetic_foot_issues": {
        "disease_name": "Diabetic Foot Issues",
        "symptoms": ["foot ulcers", "neuropathy", "poor wound healing"],
        "why": "Diabetes causes nerve damage and poor circulation.",
        "medicines": ["Antibiotics", "Pain management", "Growth factors"],
        "home_remedies": ["Foot care", "Regular inspection", "Proper footwear"],
        "critical_conditions": ["Gangrene", "Amputation"],
        "doctor_advice": "Regular foot care and diabetes control essential.",
        "doctor_type": "Podiatrist, Endocrinologist"
    },
    "diabetic_ketoacidosis": {
        "disease_name": "Diabetic Ketoacidosis (DKA)",
        "symptoms": ["severe hyperglycemia", "ketosis", "acidosis", "Kussmaul breathing"],
        "why": "Insulin deficiency causes uncontrolled glucose and ketone production.",
        "medicines": ["Insulin", "IV fluids", "Electrolyte replacement"],
        "home_remedies": ["None - requires hospitalization"],
        "critical_conditions": ["DKA itself", "Coma", "Death"],
        "doctor_advice": "Call emergency services immediately.",
        "doctor_type": "Endocrinologist, Emergency Medicine"
    },
    "diabetic_retinopathy": {
        "disease_name": "Diabetic Retinopathy",
        "symptoms": ["vision changes", "floaters", "blurred vision", "vision loss"],
        "why": "High blood sugar damages blood vessels in retina.",
        "medicines": ["Anti-VEGF injections", "Laser therapy"],
        "home_remedies": ["Tight glucose control", "Blood pressure management"],
        "critical_conditions": ["Blindness"],
        "doctor_advice": "Regular eye exams and strict diabetes control essential.",
        "doctor_type": "Ophthalmologist"
    },
    "diarrhoea_adults": {
        "disease_name": "Diarrhoea in Adults",
        "symptoms": ["frequent loose stools", "abdominal pain", "dehydration"],
        "why": "Infection, food intolerance, or medications cause increased bowel movements.",
        "medicines": ["Antidiarrheals", "Antibiotics if bacterial"],
        "home_remedies": ["Fluids", "BRAT diet", "Rest"],
        "critical_conditions": ["Severe dehydration", "Sepsis"],
        "doctor_advice": "Stay hydrated. Seek medical care if diarrhea persists.",
        "doctor_type": "Gastroenterologist"
    },
    "diarrhoea_children": {
        "disease_name": "Diarrhoea in Children and Babies",
        "symptoms": ["frequent loose stools", "dehydration", "fever"],
        "why": "Viral or bacterial infection causes diarrhea in children.",
        "medicines": ["Oral rehydration", "Probiotics"],
        "home_remedies": ["Breast milk or formula", "Age-appropriate foods"],
        "critical_conditions": ["Severe dehydration", "Malnutrition"],
        "doctor_advice": "Monitor for dehydration. Seek medical care immediately if severe.",
        "doctor_type": "Pediatrician"
    },
    "discoid_eczema": {
        "disease_name": "Discoid Eczema",
        "symptoms": ["circular red patches", "itching", "oozing", "scaling"],
        "why": "Inflammatory skin condition causes distinctive coin-shaped lesions.",
        "medicines": ["Topical corticosteroids", "Emollients"],
        "home_remedies": ["Moisturizing", "Avoid irritants", "Cool compresses"],
        "critical_conditions": ["Secondary infection"],
        "doctor_advice": "Consult dermatologist for diagnosis.",
        "doctor_type": "Dermatologist"
    },
    "diverticular_disease": {
        "disease_name": "Diverticular Disease and Diverticulitis",
        "symptoms": ["lower abdominal pain", "fever", "constipation or diarrhea"],
        "why": "Colonic outpouchings become inflamed or infected.",
        "medicines": ["Antibiotics", "Pain management", "Anti-inflammatory drugs"],
        "home_remedies": ["Bowel rest", "Clear liquids initially"],
        "critical_conditions": ["Perforation", "Peritonitis", "Sepsis"],
        "doctor_advice": "Requires medical evaluation. May need hospitalization.",
        "doctor_type": "Gastroenterologist, Colorectal Surgeon"
    },
    "dizziness": {
        "disease_name": "Dizziness (Lightheadedness)",
        "symptoms": ["lightheadedness", "vertigo", "imbalance", "nausea"],
        "why": "Various causes affect balance and inner ear function.",
        "medicines": ["Meclizine", "Antihistamines"],
        "home_remedies": ["Rest", "Gradual position changes", "Hydration"],
        "critical_conditions": ["Severe vertigo", "Syncope"],
        "doctor_advice": "Identify underlying cause.",
        "doctor_type": "Neurologist, ENT"
    },
    "downs_syndrome": {
        "disease_name": "Down's Syndrome",
        "symptoms": ["intellectual disability", "low muscle tone", "facial features"],
        "why": "Trisomy 21 causes chromosomal abnormality.",
        "medicines": ["Symptom-specific medications"],
        "home_remedies": ["Early intervention", "Education", "Support services"],
        "critical_conditions": ["Congenital heart disease", "Leukemia"],
        "doctor_advice": "Requires multidisciplinary care and family support.",
        "doctor_type": "Pediatrician, Developmental Specialist"
    },
    "dry_mouth": {
        "disease_name": "Dry Mouth",
        "symptoms": ["dry mouth", "difficulty swallowing", "mouth sores", "taste changes"],
        "why": "Reduced saliva production from various causes.",
        "medicines": ["Saliva substitutes", "Pilocarpine"],
        "home_remedies": ["Frequent sips of water", "Sugar-free gum", "Oral care"],
        "critical_conditions": ["Severe infections", "Difficulty eating"],
        "doctor_advice": "Identify underlying cause.",
        "doctor_type": "Dentist, General Practitioner"
    },
    "duchenne_muscular_dystrophy": {
        "disease_name": "Duchenne Muscular Dystrophy (DMD)",
        "symptoms": ["progressive muscle weakness", "difficulty walking", "calf enlargement"],
        "why": "Genetic mutation prevents dystrophin production.",
        "medicines": ["Corticosteroids", "Supportive care"],
        "home_remedies": ["Physical therapy", "Orthotic devices"],
        "critical_conditions": ["Cardiomyopathy", "Respiratory failure"],
        "doctor_advice": "Requires neurologist care and supportive treatment.",
        "doctor_type": "Neurologist, Genetic Counselor"
    },
    "dysphagia": {
        "disease_name": "Dysphagia (Swallowing Problems)",
        "symptoms": ["difficulty swallowing", "choking", "food regurgitation"],
        "why": "Neurological or anatomical problems affect swallowing.",
        "medicines": ["None specific"],
        "home_remedies": ["Swallowing therapy", "Modified diet", "Speech therapy"],
        "critical_conditions": ["Aspiration pneumonia", "Malnutrition"],
        "doctor_advice": "Swallow study and speech therapy recommended.",
        "doctor_type": "Speech Therapist, Gastroenterologist"
    },
    "dystonia": {
        "disease_name": "Dystonia",
        "symptoms": ["involuntary muscle contractions", "abnormal postures", "tremor"],
        "why": "Basal ganglia dysfunction causes muscle tone abnormalities.",
        "medicines": ["Botulinum toxin", "Anticholinergics"],
        "home_remedies": ["Occupational therapy", "Relaxation"],
        "critical_conditions": ["Status dystonicus"],
        "doctor_advice": "Requires neurologist evaluation and management.",
        "doctor_type": "Neurologist"
    },
    "eating_disorders": {
        "disease_name": "Eating Disorders",
        "symptoms": ["disordered eating patterns", "weight abnormalities", "psychological issues"],
        "why": "Psychological and biological factors cause abnormal eating patterns.",
        "medicines": ["Antidepressants", "Nutritional support"],
        "home_remedies": ["Cognitive behavioral therapy", "Support groups"],
        "critical_conditions": ["Malnutrition", "Electrolyte imbalance"],
        "doctor_advice": "Requires psychiatric and medical intervention.",
        "doctor_type": "Psychiatrist, Internist"
    },
    "earache": {
        "disease_name": "Earache",
        "symptoms": ["ear pain", "hearing problems", "ear discharge"],
        "why": "Infection or inflammation of ear structures.",
        "medicines": ["Antibiotics", "Pain relievers", "Ear drops"],
        "home_remedies": ["Warm compress", "Garlic oil"],
        "critical_conditions": ["Hearing loss", "Mastoiditis"],
        "doctor_advice": "See doctor for diagnosis. May need antibiotics.",
        "doctor_type": "ENT Specialist"
    },
    "early_miscarriage": {
        "disease_name": "Early Miscarriage",
        "symptoms": ["vaginal bleeding", "abdominal pain", "cessation of pregnancy symptoms"],
        "why": "Embryonic or fetal loss in first trimester.",
        "medicines": ["Supportive care", "Rh immunoglobulin if needed"],
        "home_remedies": ["Rest", "Emotional support"],
        "critical_conditions": ["Hemorrhage", "Infection"],
        "doctor_advice": "Requires medical evaluation and follow-up.",
        "doctor_type": "Gynecologist, Obstetrician"
    },
    "earwax_buildup": {
        "disease_name": "Earwax Build-up",
        "symptoms": ["hearing loss", "ear fullness", "ear discomfort"],
        "why": "Excessive earwax accumulation blocks ear canal.",
        "medicines": ["Ear drops", "Professional removal"],
        "home_remedies": ["Warm water irrigation"],
        "critical_conditions": ["Conductive hearing loss"],
        "doctor_advice": "Professional earwax removal if needed.",
        "doctor_type": "ENT Specialist"
    },
    "ectopic_pregnancy": {
        "disease_name": "Ectopic Pregnancy",
        "symptoms": ["abdominal pain", "vaginal bleeding", "pelvic pain"],
        "why": "Pregnancy develops outside uterus.",
        "medicines": ["Methotrexate", "Surgical intervention"],
        "home_remedies": ["None - requires medical intervention"],
        "critical_conditions": ["Rupture", "Hemorrhagic shock"],
        "doctor_advice": "Call emergency services if severe symptoms.",
        "doctor_type": "Obstetrician-Gynecologist"
    },
    "elbow_fracture": {
        "disease_name": "Elbow (Radial Head or Neck) Fracture",
        "symptoms": ["elbow pain", "swelling", "reduced arm movement"],
        "why": "Trauma fractures radial head or neck.",
        "medicines": ["Pain relievers", "Anti-inflammatory drugs"],
        "home_remedies": ["Immobilization", "Ice", "Elevation"],
        "critical_conditions": ["Non-union", "Nerve damage"],
        "doctor_advice": "X-rays needed. Most heal with conservative treatment.",
        "doctor_type": "Orthopedist"
    },
    "edwards_syndrome": {
        "disease_name": "Edwards' Syndrome",
        "symptoms": ["multiple congenital abnormalities", "intellectual disability"],
        "why": "Trisomy 18 chromosomal abnormality.",
        "medicines": ["Supportive care only"],
        "home_remedies": ["Comfort care", "Family support"],
        "critical_conditions": ["Organ abnormalities", "Usually fatal"],
        "doctor_advice": "Requires palliative and family support.",
        "doctor_type": "Pediatrician, Genetic Counselor"
    },
    "emery_dreifuss_muscular_dystrophy": {
        "disease_name": "Emery-Dreifuss Muscular Dystrophy",
        "symptoms": ["progressive muscle weakness", "joint contractures", "cardiac involvement"],
        "why": "Genetic mutation affects nuclear membrane proteins.",
        "medicines": ["Cardiac medications", "Supportive care"],
        "home_remedies": ["Physical therapy", "Cardiac monitoring"],
        "critical_conditions": ["Cardiomyopathy", "Arrhythmias"],
        "doctor_advice": "Requires genetic and cardiac specialist care.",
        "doctor_type": "Neurologist, Cardiologist"
    },
    "endometriosis": {
        "disease_name": "Endometriosis",
        "symptoms": ["severe menstrual pain", "dyspareunia", "pelvic pain", "infertility"],
        "why": "Uterine lining grows outside uterus causing inflammation.",
        "medicines": ["Hormonal contraceptives", "Progestins", "GnRH agonists"],
        "home_remedies": ["Heat therapy", "Regular exercise", "Dietary changes"],
        "critical_conditions": ["Severe adhesions", "Infertility"],
        "doctor_advice": "Requires gynecology care. May need surgery.",
        "doctor_type": "Gynecologist"
    },
    "epilepsy": {
        "disease_name": "Epilepsy",
        "symptoms": ["recurrent seizures", "loss of consciousness", "muscle convulsions"],
        "why": "Abnormal electrical brain activity causes seizures.",
        "medicines": ["Antiepileptic drugs", "Seizure management medications"],
        "home_remedies": ["Avoid triggers", "Sleep hygiene", "Stress management"],
        "critical_conditions": ["Status epilepticus", "SUDEP"],
        "doctor_advice": "Requires neurologist care and medication management.",
        "doctor_type": "Neurologist"
    },
    "erectile_dysfunction": {
        "disease_name": "Erectile Dysfunction (Impotence)",
        "symptoms": ["inability to achieve/maintain erection", "reduced libido"],
        "why": "Vascular, neurological, or psychological causes.",
        "medicines": ["PDE5 inhibitors", "Hormone therapy"],
        "home_remedies": ["Lifestyle changes", "Psychological counseling"],
        "critical_conditions": ["Relationship dysfunction"],
        "doctor_advice": "Consult urologist. May indicate underlying disease.",
        "doctor_type": "Urologist"
    },
    "e_coli_o157": {
        "disease_name": "Escherichia coli (E. coli) O157",
        "symptoms": ["severe diarrhea", "bloody diarrhea", "abdominal pain"],
        "why": "Shiga toxin-producing E. coli infection.",
        "medicines": ["Supportive care", "No antibiotics usually"],
        "home_remedies": ["Fluid replacement", "Rest"],
        "critical_conditions": ["HUS", "Kidney failure"],
        "doctor_advice": "Requires medical evaluation and monitoring.",
        "doctor_type": "Gastroenterologist, Infectious Disease"
    },
    "ewing_sarcoma": {
        "disease_name": "Ewing Sarcoma",
        "symptoms": ["bone pain", "swelling", "fractures"],
        "why": "Malignant bone tumor most common in children.",
        "medicines": ["Chemotherapy", "Radiation", "Surgery"],
        "home_remedies": ["Supportive care"],
        "critical_conditions": ["Metastasis"],
        "doctor_advice": "Requires immediate oncology and orthopedic evaluation.",
        "doctor_type": "Pediatric Oncologist, Orthopedic Surgeon"
    },
    "excessive_sweating": {
        "disease_name": "Excessive Sweating (Hyperhidrosis)",
        "symptoms": ["profuse sweating", "wet clothing", "social embarrassment"],
        "why": "Overactive sweat glands from various causes.",
        "medicines": ["Antiperspirants", "Botulinum toxin injections"],
        "home_remedies": ["Cotton clothing", "Avoid triggers"],
        "critical_conditions": ["Severe dehydration", "Electrolyte loss"],
        "doctor_advice": "See dermatologist for treatment options.",
        "doctor_type": "Dermatologist"
    },
    "eye_cancer": {
        "disease_name": "Eye Cancer",
        "symptoms": ["vision changes", "eye pain", "eye mass"],
        "why": "Malignant cells develop in eye tissues.",
        "medicines": ["Chemotherapy", "Radiation", "Surgery"],
        "home_remedies": ["Supportive care"],
        "critical_conditions": ["Vision loss", "Metastasis"],
        "doctor_advice": "Requires immediate ophthalmology and oncology care.",
        "doctor_type": "Ophthalmologist, Oncologist"
    },
    "facioscapulohumeral_muscular_dystrophy": {
        "disease_name": "Facioscapulohumeral Muscular Dystrophy (FSHD)",
        "symptoms": ["facial weakness", "shoulder blade winging", "progressive weakness"],
        "why": "Genetic mutation causes muscle protein deficiency.",
        "medicines": ["Corticosteroids", "Supportive care"],
        "home_remedies": ["Physical therapy", "Occupational therapy"],
        "critical_conditions": ["Respiratory involvement", "Hearing loss"],
        "doctor_advice": "Requires neurologist care and physical therapy.",
        "doctor_type": "Neurologist"
    },
    "farting": {
        "disease_name": "Flatulence",
        "symptoms": ["excessive gas", "bloating", "flatulence"],
        "why": "Intestinal gas from fermentation or swallowed air.",
        "medicines": ["Simethicone", "Probiotics"],
        "home_remedies": ["Dietary changes", "Slow eating", "Herbal teas"],
        "critical_conditions": ["Indicates underlying GI issues"],
        "doctor_advice": "Usually benign. Consult doctor if accompanied by pain.",
        "doctor_type": "Gastroenterologist"
    },
    "febrile_seizures": {
        "disease_name": "Febrile Seizures",
        "symptoms": ["seizures during fever", "loss of consciousness", "muscle rigidity"],
        "why": "High fever triggers seizures in susceptible young children.",
        "medicines": ["Fever management", "Anticonvulsants if recurrent"],
        "home_remedies": ["Fever control", "Temperature monitoring"],
        "critical_conditions": ["Status epilepticus", "Febrile status"],
        "doctor_advice": "Call doctor immediately if seizure occurs.",
        "doctor_type": "Pediatrician, Neurologist"
    },
    "feeling_something_throat": {
        "disease_name": "Feeling of Something in Throat (Globus)",
        "symptoms": ["throat fullness", "difficulty swallowing", "sensation of lump"],
        "why": "Muscle tension or psychological causes sensation.",
        "medicines": ["Relaxants", "Antidepressants"],
        "home_remedies": ["Relaxation techniques", "Voice therapy"],
        "critical_conditions": ["Actually indicates pathology if persistent"],
        "doctor_advice": "See ENT to rule out organic causes.",
        "doctor_type": "ENT Specialist"
    },
    "fever_adults": {
        "disease_name": "Fever in Adults",
        "symptoms": ["elevated temperature", "chills", "malaise"],
        "why": "Body's immune response to infection or inflammation.",
        "medicines": ["Acetaminophen", "Ibuprofen"],
        "home_remedies": ["Rest", "Fluids", "Cool compresses"],
        "critical_conditions": ["Very high fever", "Underlying serious infection"],
        "doctor_advice": "Identify cause. Seek medical care if >103°F or prolonged.",
        "doctor_type": "General Practitioner"
    },
    "fever_children": {
        "disease_name": "Fever in Children",
        "symptoms": ["elevated temperature", "fussiness", "reduced activity"],
        "why": "Body's immune response to infection.",
        "medicines": ["Acetaminophen", "Ibuprofen"],
        "home_remedies": ["Fluids", "Light clothing", "Sponging"],
        "critical_conditions": ["Febrile seizures", "Severe infection"],
        "doctor_advice": "Seek medical care for high fever or if concerned.",
        "doctor_type": "Pediatrician"
    },
    "fibroids": {
        "disease_name": "Fibroids",
        "symptoms": ["heavy menstrual bleeding", "pelvic pain", "pressure"],
        "why": "Benign uterine tumors grow in muscle layer.",
        "medicines": ["Hormonal medications", "GnRH agonists"],
        "home_remedies": ["Nutritious diet", "Regular exercise"],
        "critical_conditions": ["Severe bleeding causing anemia"],
        "doctor_advice": "Requires gynecology evaluation.",
        "doctor_type": "Gynecologist"
    },
    "fibromyalgia": {
        "disease_name": "Fibromyalgia",
        "symptoms": ["widespread pain", "fatigue", "sleep problems", "cognitive issues"],
        "why": "Central nervous system sensitization amplifies pain signals.",
        "medicines": ["Antidepressants", "Anticonvulsants", "Pain relievers"],
        "home_remedies": ["Regular exercise", "Sleep hygiene", "Stress management"],
        "critical_conditions": ["Severe disability"],
        "doctor_advice": "Requires multidisciplinary approach.",
        "doctor_type": "Rheumatologist"
    },
    "flat_feet_children": {
        "disease_name": "Flat Feet in Children and Young People",
        "symptoms": ["flat foot appearance", "foot pain", "walking difficulty"],
        "why": "Arch fails to develop properly.",
        "medicines": ["Pain relievers if needed"],
        "home_remedies": ["Special insoles", "Stretching exercises"],
        "critical_conditions": ["Posterior tibial tendon dysfunction"],
        "doctor_advice": "Usually self-limiting. See pediatrician if problematic.",
        "doctor_type": "Pediatrician, Podiatrist"
    },
    "flu": {
        "disease_name": "Flu (Influenza)",
        "symptoms": ["fever", "cough", "body ache", "sore throat"],
        "why": "Influenza virus infects respiratory tract.",
        "medicines": ["Antivirals", "Symptom relief"],
        "home_remedies": ["Rest", "Fluids", "Gargling"],
        "critical_conditions": ["Severe pneumonia", "Respiratory failure"],
        "doctor_advice": "Antivirals most effective within 48 hours.",
        "doctor_type": "General Practitioner"
    },
    "foetal_alcohol_syndrome": {
        "disease_name": "Foetal Alcohol Syndrome",
        "symptoms": ["intellectual disability", "facial abnormalities", "growth problems"],
        "why": "Maternal alcohol exposure causes fetal damage.",
        "medicines": ["Supportive care"],
        "home_remedies": ["Early intervention", "Special education"],
        "critical_conditions": ["Severe disabilities"],
        "doctor_advice": "Requires multidisciplinary care.",
        "doctor_type": "Pediatrician, Developmental Specialist"
    },
    "food_allergy": {
        "disease_name": "Food Allergy",
        "symptoms": ["itching", "swelling", "rash", "anaphylaxis"],
        "why": "Immune system overreacts to food protein.",
        "medicines": ["Antihistamines", "Epinephrine if severe"],
        "home_remedies": ["Allergen avoidance"],
        "critical_conditions": ["Anaphylaxis"],
        "doctor_advice": "Allergy testing important. EpiPen if severe.",
        "doctor_type": "Allergist"
    },
    "food_poisoning": {
        "disease_name": "Food Poisoning",
        "symptoms": ["nausea", "vomiting", "diarrhea", "abdominal pain"],
        "why": "Contaminated food contains bacteria or toxins.",
        "medicines": ["Anti-nausea medication", "Antibiotics if severe"],
        "home_remedies": ["Fluids", "Bland diet", "Rest"],
        "critical_conditions": ["Severe dehydration", "Sepsis"],
        "doctor_advice": "Stay hydrated. Seek care if severe.",
        "doctor_type": "Gastroenterologist"
    },
    "fragility_fracture_hip": {
        "disease_name": "Fragility Fracture of the Hip",
        "symptoms": ["hip pain", "inability to walk", "swelling"],
        "why": "Osteoporotic bone breaks easily from fall.",
        "medicines": ["Pain management", "Bone-protective medications"],
        "home_remedies": ["Immobilization", "Physical therapy"],
        "critical_conditions": ["Non-union", "Infection"],
        "doctor_advice": "Requires surgery usually. Bone health evaluation needed.",
        "doctor_type": "Orthopedic Surgeon"
    },
    "frozen_shoulder": {
        "disease_name": "Frozen Shoulder",
        "symptoms": ["shoulder pain", "stiffness", "limited movement"],
        "why": "Shoulder joint inflammation and tissue thickening.",
        "medicines": ["NSAIDs", "Corticosteroid injections"],
        "home_remedies": ["Physical therapy", "Heat therapy", "Stretching"],
        "critical_conditions": ["Persistent stiffness"],
        "doctor_advice": "Physical therapy essential. May take months to resolve.",
        "doctor_type": "Orthopedist, Physical Therapist"
    },
    "functional_neurological_disorder": {
        "disease_name": "Functional Neurological Disorder (FND)",
        "symptoms": ["neurological symptoms without neurological cause", "varied symptoms"],
        "why": "Psychological stress manifests as neurological symptoms.",
        "medicines": ["Antidepressants", "Anxiolytics"],
        "home_remedies": ["Cognitive behavioral therapy", "Psychiatry"],
        "critical_conditions": ["Severe disability"],
        "doctor_advice": "Requires neurologist and psychiatrist collaboration.",
        "doctor_type": "Neurologist, Psychiatrist"
    },
    "fungal_nail_infection": {
        "disease_name": "Fungal Nail Infection",
        "symptoms": ["nail discoloration", "thickening", "crumbling"],
        "why": "Fungal overgrowth in nail bed.",
        "medicines": ["Antifungal medications", "Topical treatments"],
        "home_remedies": ["Keep nails dry", "Trim regularly"],
        "critical_conditions": ["Complete nail destruction"],
        "doctor_advice": "Requires prolonged antifungal treatment.",
        "doctor_type": "Dermatologist"
    },
    "gallbladder_cancer": {
        "disease_name": "Gallbladder Cancer",
        "symptoms": ["abdominal pain", "jaundice", "weight loss"],
        "why": "Malignant cells develop in gallbladder.",
        "medicines": ["Chemotherapy", "Radiation"],
        "home_remedies": ["Nutritional support"],
        "critical_conditions": ["Bile duct obstruction", "Liver failure"],
        "doctor_advice": "Requires immediate oncology evaluation.",
        "doctor_type": "Oncologist, Hepatobiliary Surgeon"
    },
    "gallstones": {
        "disease_name": "Gallstones",
        "symptoms": ["right upper abdominal pain", "nausea", "pain after fatty meals"],
        "why": "Cholesterol or bilirubin precipitate into stones.",
        "medicines": ["Ursodeoxycholic acid for small stones", "Pain management"],
        "home_remedies": ["Low fat diet"],
        "critical_conditions": ["Cholecystitis", "Pancreatitis"],
        "doctor_advice": "Surgery if symptomatic.",
        "doctor_type": "Surgeon, Gastroenterologist"
    },
    "ganglion_cyst": {
        "disease_name": "Ganglion Cyst",
        "symptoms": ["visible bump", "pain", "nerve compression"],
        "why": "Fluid-filled cyst develops on joint or tendon.",
        "medicines": ["NSAIDs", "Corticosteroid injections"],
        "home_remedies": ["Activity modification", "Ice"],
        "critical_conditions": ["Nerve compression", "Vascular compromise"],
        "doctor_advice": "Usually benign. Surgery if symptomatic.",
        "doctor_type": "Orthopedist"
    },
    "gastroenteritis_adults": {
        "disease_name": "Gastroenteritis in Adults",
        "symptoms": ["diarrhea", "vomiting", "abdominal pain", "fever"],
        "why": "Viral or bacterial infection affects GI tract.",
        "medicines": ["Anti-nausea medications", "Antibiotics if bacterial"],
        "home_remedies": ["Rehydration", "Bland diet", "Rest"],
        "critical_conditions": ["Dehydration", "Sepsis"],
        "doctor_advice": "Stay hydrated. Most resolve without treatment.",
        "doctor_type": "Gastroenterologist"
    },
    "gastroenteritis_children": {
        "disease_name": "Gastroenteritis in Children and Babies",
        "symptoms": ["diarrhea", "vomiting", "dehydration", "fever"],
        "why": "Viral infection common in children.",
        "medicines": ["Rehydration solutions"],
        "home_remedies": ["Breast milk or formula", "Frequent feeding"],
        "critical_conditions": ["Severe dehydration", "Sepsis"],
        "doctor_advice": "Monitor hydration closely in children.",
        "doctor_type": "Pediatrician"
    },
    "gord": {
        "disease_name": "Gastro-Oesophageal Reflux Disease (GORD)",
        "symptoms": ["heartburn", "regurgitation", "chest pain", "dysphagia"],
        "why": "Stomach acid refluxes into esophagus due to weak LES.",
        "medicines": ["Proton pump inhibitors", "H2 blockers", "Antacids"],
        "home_remedies": ["Raise bed head", "Avoid triggers", "Small meals"],
        "critical_conditions": ["Barrett's esophagus", "Esophageal cancer"],
        "doctor_advice": "Lifestyle modifications first. Medication if needed.",
        "doctor_type": "Gastroenterologist"
    },
    "generalised_anxiety_disorder": {
        "disease_name": "Generalised Anxiety Disorder (GAD)",
        "symptoms": ["persistent worry", "restlessness", "difficulty concentrating"],
        "why": "Brain neurochemistry causes excessive worry.",
        "medicines": ["SSRIs", "SNRIs", "Anxiolytics"],
        "home_remedies": ["Cognitive behavioral therapy", "Relaxation techniques"],
        "critical_conditions": ["Panic attacks", "Suicide risk"],
        "doctor_advice": "Requires psychiatry and therapy support.",
        "doctor_type": "Psychiatrist, Psychologist"
    },
    "genital_herpes": {
        "disease_name": "Genital Herpes",
        "symptoms": ["genital blistering", "dysuria", "vaginal discharge"],
        "why": "Herpes simplex virus infects genital tract.",
        "medicines": ["Antivirals", "Pain relievers"],
        "home_remedies": ["Saline baths", "Avoid triggers"],
        "critical_conditions": ["Neonatal herpes", "Encephalitis"],
        "doctor_advice": "Antivirals reduce severity.",
        "doctor_type": "Gynecologist"
    },
}

