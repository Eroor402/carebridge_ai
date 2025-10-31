import streamlit as st

def load_custom_css():
    with open("styles/theme.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_custom_css()

from utils import get_session_ids, get_patient_summary, get_session_by_id

st.set_page_config(page_title="CareBridge AI — Patient Portal", layout="wide")

# Sidebar
st.sidebar.title("My Appointments")
session_id = st.sidebar.selectbox("Choose Appointment", get_session_ids(status_filter="completed"))

session = get_session_by_id(session_id)
patient = session["patient"]

# Main Panel
st.title("Patient Portal 💬")
st.subheader(f"Welcome, {patient['name']}!")
st.markdown(f"**Session ID:** {session_id}")
st.markdown(f"**Date:** {session['timestamp'].split('T')[0]}")

# Patient Summary
st.subheader("Your Health Summary")
st.write(get_patient_summary(session_id))

# Health Tips
st.subheader("Health Tips")
for code, tip in session.get("health_tips", {}).items():
    st.markdown(f"**{code}**: {tip}")

# Optional download
st.download_button("Download Summary", get_patient_summary(session_id), file_name=f"{session_id}_summary.txt")
