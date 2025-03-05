import re
import random
import string
import streamlit as st

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.markdown("Enter a password below to check its strength and get improvement suggestions.")
password = st.text_input("Enter your password:", type="password")

def display_feedback(feedback):
    for tip in feedback:
        st.write(tip)

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        
        if score == 4:
            st.success("✅ Strong Password! Your password meets all security requirements.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features like numbers or special characters.")
            display_feedback(feedback)
            strong_password = generate_strong_password()
            st.info(f"🔹 Suggested Strong Password: `{strong_password}`")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
            display_feedback(feedback)
            strong_password = generate_strong_password()
            st.info(f"🔹 Suggested Strong Password: `{strong_password}`")
    else:
        st.error("❌ Please enter a password!")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.code(strong_password, language='')

st.markdown("---")
st.subheader("💡 Tips for a Strong Password")
st.write("- Use at least 12 characters.")
st.write("- Mix uppercase, lowercase, numbers, and special characters.")
st.write("- Avoid common words and predictable sequences.")
st.write("- Consider using a password manager for secure storage.")
