import streamlit as st

st.set_page_config(page_title="CareBridge AI", layout="centered")

# 🔷 Branding and Welcome
st.title("Welcome to CareBridge AI 👋")
st.markdown("Your bridge between clinical insight and patient clarity.")

st.markdown("### Please select your role to continue:")
role = st.radio("Login as:", ["Doctor", "Patient"])

# 🔗 Navigation to Portals
if role == "Doctor":
    st.page_link("pages/doctor_portal.py", label="🩺 Go to Doctor Portal")
elif role == "Patient":
    st.page_link("pages/patient_portal.py", label="💬 Go to Patient Portal")

# 🔻 Footer
st.markdown("---")
st.markdown(
    "<center><small>CareBridge AI © 2025</small></center>",
    unsafe_allow_html=True
)