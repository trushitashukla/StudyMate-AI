import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

import streamlit as st
from PyPDF2 import PdfReader

st.title("📚 StudyMate AI")

page = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Home",
        "Study Planner",
        "Notes Summarizer",
        "Quiz Generator",
        "AI Tutor",
        "Progress Tracker"
    ]
)

# HOME
if page == "Home":
    st.header("Welcome to StudyMate AI")
    st.write("Your Personal AI Study Companion")

# STUDY PLANNER
elif page == "Study Planner":

    st.header("Smart Study Planner")

    subject = st.text_input("Subject")

    days = st.number_input(
        "Days Until Exam",
        1,
        365,
        30
    )

    hours = st.slider(
        "Hours Per Day",
        1,
        12,
        2
    )

    if st.button("Generate Plan"):
        st.success(
            f"Study {subject} for {hours} hours daily for {days} days."
        )

# NOTES SUMMARIZER
elif page == "Notes Summarizer":

    st.header("Notes Summarizer")

    uploaded_file = st.file_uploader(
        "Upload Notes",
        type=["pdf", "txt"]
    )

    text = ""

    if uploaded_file:

        st.success("File Uploaded Successfully")

        if uploaded_file.type == "text/plain":

            text = uploaded_file.read().decode("utf-8")

        elif uploaded_file.type == "application/pdf":

            pdf = PdfReader(uploaded_file)

            for pdf_page in pdf.pages:
                extracted = pdf_page.extract_text()

                if extracted:
                    text += extracted

        st.subheader("Notes Content")

        st.text_area(
            "Content",
            text,
            height=250
        )

        if st.button("Generate Summary"):

            sentences = text.split(".")

            st.subheader("Summary")

            for sentence in sentences[:5]:

                if sentence.strip():

                    st.write("•", sentence.strip())
# QUIZ GENERATOR
elif page == "Quiz Generator":

    st.header("Quiz Generator")

    notes = st.text_area(
        "Paste Notes Here",
        height=200
    )

    if st.button("Generate Quiz"):

        sentences = notes.split(".")

        count = 1

        for sentence in sentences[:5]:

            sentence = sentence.strip()

            if len(sentence) > 10:

                st.write(
                    f"Q{count}. Explain:"
                )

                st.write(sentence)

                st.text_input(
                    f"Your Answer {count}"
                )

                count += 1
# AI TUTOR
elif page == "AI Tutor":

    st.header("🤖 AI Tutor")

    question = st.text_input(
        "Ask any study-related question"
    )

    if st.button("Get Answer"):

        if question:

            with st.spinner("Thinking..."):

                response = model.generate_content(
                    f"Explain this in simple language for a student: {question}"
                )

                st.success("Answer Generated")

                st.write(response.text)

# PROGRESS TRACKER
elif page == "Progress Tracker":

    st.header("📈 Progress Tracker")

    st.metric(
        "Quizzes Completed",
        12
    )

    st.metric(
        "Average Score",
        "82%"
    )

    st.metric(
        "Study Streak",
        "5 Days"
    )

    st.progress(82)

    st.success(
        "Great job! Keep studying consistently."
    )