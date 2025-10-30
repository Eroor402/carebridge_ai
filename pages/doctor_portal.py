import streamlit as st
from utils import get_session_ids, get_doctor_summary, get_structured_ehr, get_session_by_id, save_new_session

from audiorecorder import audiorecorder
import speech_recognition as sr
from utils import save_new_session
from io import BytesIO

st.set_page_config(page_title="CareBridge AI — Doctor Portal", layout="wide")

# Sidebar
st.sidebar.title("Session Controls")
session_id = st.sidebar.selectbox("Choose Appointment", get_session_ids())

session = get_session_by_id(session_id)
patient = session["patient"]

st.subheader("🎙️ Record Voice Notes")

# Initialize transcription
transcription = ""

from audiorecorder import audiorecorder
import streamlit as st
import speech_recognition as sr
from io import BytesIO

# Record audio
audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # Convert AudioSegment to bytes
    audio_bytes = BytesIO()
    audio.export(audio_bytes, format="wav")
    audio_bytes.seek(0)

    # Play audio in Streamlit
    st.audio(audio_bytes.read(), format="audio/wav")

    # Save file for recognition
    with open("temp.wav", "wb") as f:
        audio.export(f, format="wav")

    # Speech recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        try:
            transcription = recognizer.recognize_google(audio_data)
            st.success("Transcription successful!")
            st.write("**Transcription:**", transcription)
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("Speech recognition service failed.")

# 🧾 Form to create session
st.subheader("Start New Appointment")

with st.form("new_session_form"):
    patient_name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    transcription_input = st.text_area("Transcribed Notes", value=transcription, height=150)
    submitted = st.form_submit_button("Create Session")

    if submitted:
        new_id = save_new_session(patient_name, age, gender, transcription_input)
        st.success(f"New session created: {new_id}")
        st.experimental_rerun()

# Main Panel
st.title("Doctor Portal")
st.subheader(f"Patient: {patient['name']} ({patient['age']}Y, {patient['gender']})")
st.markdown(f"**Session ID:** {session_id}")
st.markdown(f"**Status:** {session['status'].capitalize()}")

tab1, tab2, tab3 = st.tabs(["📝 Transcription", "📋 Structured EHR", "🧠 Summary"])

with tab1:
    st.write(session["transcription"])

with tab2:
    st.write(get_structured_ehr(session_id))

with tab3:
    st.write(get_doctor_summary(session_id))

if session["status"] == "active":
    if st.button("Mark Session as Completed"):
        from utils import mark_session_completed
        mark_session_completed(session_id)
        st.success(f"Session {session_id} marked as completed.")
        st.experimental_rerun()
