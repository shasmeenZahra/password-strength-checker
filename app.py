import streamlit as st
import random
import string
import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1
    
    if score == 5:
        return "🟢 Strong"
    elif score >= 3:
        return "🟡 Moderate"
    else:
        return "🔴 Weak"

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "@$!%*?&"
    return ''.join(random.choice(characters) for _ in range(12))

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.markdown(
    """<h1 style='text-align: center; color: #ff9900;'>🔐 Password Strength Meter</h1>""",
    unsafe_allow_html=True
)

st.write("Check your password strength and get improvement suggestions!")

name = st.text_input("Enter your name:", key="name")
password = st.text_input("Enter your password:", type="password", key="password")

col1, col2 = st.columns(2)

with col1:
    if st.button("Check Strength", use_container_width=True):
        if password:
            strength = check_password_strength(password)
            st.success(f"Password Strength: {strength}")
        else:
            st.warning("Please enter a password!")

with col2:
    if st.button("Generate Strong Password", use_container_width=True):
        strong_password = generate_strong_password()
        st.info(f"Generated Password: `{strong_password}`")

st.markdown("---")
st.markdown("🔐 **Secure Your Digital Life with Strong Passwords!**")
st.markdown("⚡ **Stay Safe, Stay Protected!**")
