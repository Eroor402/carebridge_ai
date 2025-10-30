import json

DATA_FILE = "data/carebridge_mock_data.json"

# Load all sessions from the JSON file
def load_all_sessions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Get session IDs (optionally filter by status: 'completed', 'active')
def get_session_ids(status_filter=None):
    sessions = load_all_sessions()
    if status_filter:
        sessions = [s for s in sessions if s["status"] == status_filter]
    return [s["session_id"] for s in sessions]

# Get full session data by ID
def get_session_by_id(session_id):
    sessions = load_all_sessions()
    for s in sessions:
        if s["session_id"] == session_id:
            return s
    return None

# Get patient summary (plain language)
def get_patient_summary(session_id):
    session = get_session_by_id(session_id)
    return session["summaries"]["patient_view"]

# Get doctor summary (clinical)
def get_doctor_summary(session_id):
    session = get_session_by_id(session_id)
    return session["summaries"]["doctor_view"]

# Get structured EHR data
def get_structured_ehr(session_id):
    session = get_session_by_id(session_id)
    return session["ehr"]

# Get health tips based on ICD code
def get_health_tips(session_id):
    session = get_session_by_id(session_id)
    return session.get("health_tips", {})

from datetime import datetime

def save_new_session(patient_name, age, gender, transcription):
    sessions = load_all_sessions()
    new_id = f"session_{len(sessions)+1:03d}"
    timestamp = datetime.now().isoformat()

    new_session = {
        "session_id": new_id,
        "timestamp": timestamp,
        "status": "active",
        "patient": {
            "name": patient_name,
            "age": age,
            "gender": gender
        },
        "transcription": transcription,
        "ehr": {},
        "summaries": {},
        "health_tips": {}
    }

    # 🔮 Enrich session
    enriched = enrich_session(new_session)
    sessions.append(enriched)

    with open(DATA_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

    return new_id

def mark_session_completed(session_id):
    sessions = load_all_sessions()
    for s in sessions:
        if s["session_id"] == session_id:
            s["status"] = "completed"
            break
    with open(DATA_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

def enrich_session(session):
    text = session["transcription"].lower()

    # Diagnosis and ICD mapping
    diagnosis_map = {
        "diabetes": ("Type 2 Diabetes", "E11.9"),
        "hypertension": ("Hypertension", "I10"),
        "thyroid": ("Thyroid Disorder", "E03.9"),
        "asthma": ("Asthma", "J45.909"),
        "cholesterol": ("High Cholesterol", "E78.0")
    }

    diagnoses, icd_codes, tips = [], [], {}
    for keyword, (label, code) in diagnosis_map.items():
        if keyword in text:
            diagnoses.append(label)
            icd_codes.append(code)
            tips[code] = f"Tips for {label}: Maintain a healthy lifestyle and follow doctor's advice regularly."

    # Vitals
    import re
    bp_match = re.search(r"bp\s+(\d{2,3}/\d{2,3})", text)
    bp = bp_match.group(1) if bp_match else "N/A"

    # Medications
    meds = []
    for med in ["metformin", "losartan", "levothyroxine", "salbutamol", "atorvastatin"]:
        if med in text:
            meds.append(med.capitalize())

    # Plan
    plan = []
    if "diet" in text:
        plan.append("Diet control")
    if "exercise" in text:
        plan.append("Exercise")
    if "follow-up" in text:
        plan.append("Follow-up in 2 weeks")

    # Summaries
    age = session["patient"]["age"]
    gender = session["patient"]["gender"][0].upper()
    doc_summary = f"{age}Y, {gender}, {', '.join(diagnoses)}, BP {bp}, Rx: {', '.join(meds)}, Plan: {', '.join(plan)}."
    pat_summary = f"You have {', '.join(diagnoses).lower()} and your blood pressure was {bp}. You were prescribed {', '.join(meds)} and advised to {', '.join([p.lower() for p in plan])}."

    # Update session
    session["ehr"] = {
        "diagnoses": diagnoses,
        "icd_codes": icd_codes,
        "vitals": {"BP": bp},
        "prescriptions": meds,
        "plan": plan
    }
    session["summaries"] = {
        "doctor_view": doc_summary,
        "patient_view": pat_summary
    }
    session["health_tips"] = tips

    return session