import streamlit as st

def load_custom_css():
    with open("styles/theme.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_custom_css()

st.set_page_config(page_title="CareBridge AI", layout="centered")

# 🔷 Branding and Welcome
st.markdown("""
<div class="hero">
    <h1>Welcome to CareBridge AI 👋</h1>
    <p>Your bridge between clinical insight and patient clarity.</p>
    <p style="margin-top: 2em;"><strong>Please select your role to continue:</strong></p>
    <div class="role-cards">
        <div class="card">
            <h3>🩺 Doctor</h3>
            <p>Access session tracking, voice-to-EHR, and summaries.</p>
            <a href="/doctor_portal">Go to Doctor Portal</a>
        </div>
        <div class="card">
            <h3>👤 Patient</h3>
            <p>View summaries, track appointments, and stay informed.</p>
            <a href="/patient_portal">Go to Patient Portal</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<small class="tagline">Empowering care through clarity and connection.</small>', unsafe_allow_html=True)
st.markdown('<hr style="margin-top: 3em;">', unsafe_allow_html=True)
st.markdown('<center>CareBridge AI © 2023</center>', unsafe_allow_html=True)

# 🔻 Footer
st.markdown("---")
st.markdown(
    "<center><small>CareBridge AI © 2025</small></center>",
    unsafe_allow_html=True
)
