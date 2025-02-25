import streamlit as st
import random

# Growth Mindset Quiz Data
questions = [
    {"question": "When faced with a difficult challenge, what do you do?",
     "options": ["Give up", "Try a different approach", "Avoid it", "Blame others"], "answer": "Try a different approach"},
    
    {"question": "What is the best way to improve at something?",
     "options": ["Practice and learn from mistakes", "Wait for natural talent", "Do the same thing repeatedly", "Avoid difficult tasks"], "answer": "Practice and learn from mistakes"},
    
    {"question": "How do you feel about making mistakes?",
     "options": ["Mistakes help me learn", "I should avoid mistakes", "Mistakes mean failure", "I feel embarrassed"], "answer": "Mistakes help me learn"},
    
    {"question": "If you receive constructive criticism, what is your reaction?",
     "options": ["Ignore it", "Use it to improve", "Get upset", "Prove them wrong"], "answer": "Use it to improve"},
    
    {"question": "Which of the following is a Growth Mindset belief?",
     "options": ["I can develop my abilities", "I am born smart or dumb", "Effort doesn’t matter", "Success is only for talented people"], "answer": "I can develop my abilities"}
]

# Streamlit UI Styling
# Streamlit UI Styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            color: black;  /* Text color black kar diya */
        }
        .stButton>button {
            background-color: #28a745;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        /* Mobile Screen Fix */
        @media (max-width: 768px) {
            .main {
                padding: 15px;
                font-size: 16px;
            }
        }
    </style>
""", unsafe_allow_html=True)


st.title("🌱 Growth Mindset Quiz")
st.write("Test your mindset! Answer these questions to see if you have a growth mindset.")

# Session state to store user answers
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_question = 0
    random.shuffle(questions)

# Display current question with progress bar
q_index = st.session_state.current_question
st.progress(q_index / len(questions))

if q_index < len(questions):
    q_data = questions[q_index]
    st.markdown(f"<div class='main'><h3>Question {q_index + 1}:</h3><p>{q_data['question']}</p></div>", unsafe_allow_html=True)
    
    selected_option = st.radio("Choose an answer:", q_data["options"], index=None)
    
    if st.button("Submit Answer", help="Click to submit your answer"):
        if selected_option:
            if selected_option == q_data['answer']:
                st.session_state.score += 1
                st.success("✅ Correct! That's the Growth Mindset approach!")
            else:
                st.error("❌ Incorrect. Try to embrace a Growth Mindset!")
            
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.warning("⚠️ Please select an answer before submitting.")

# Show final result
else:
    st.subheader("Quiz Completed! 🎉")
    st.write(f"Your Growth Mindset Score: **{st.session_state.score} / {len(questions)}**")
    
    if st.session_state.score == len(questions):
        st.success("🔥 Amazing! You have a strong Growth Mindset! Keep learning!")
    elif st.session_state.score >= len(questions) // 2:
        st.info("👍 Good job! Keep practicing Growth Mindset strategies!")
    else:
        st.warning("💡 Keep working on your Growth Mindset. Challenges help you grow!")
    
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        random.shuffle(questions)
        st.rerun()

