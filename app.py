import streamlit as st
from PyPDF2 import PdfReader

st.title("📚 StudyMate AI")
st.subheader("Your Personal AI Study Companion")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome, {name}!")

subject = st.selectbox(
    "Select a subject",
    ["Python", "Database", "Web Development", "Operating System"]
)

st.write("Selected Subject:", subject)

st.divider()

# ---------------- STUDY PLANNER ----------------

st.header("Study Planner")

hours = st.slider(
    "How many hours can you study today?",
    1,
    12,
    2
)

if st.button("Generate Plan"):

    st.subheader("Today's Study Plan")

    st.write(f"📖 Study {subject} for {hours} hour(s)")
    st.write("📝 Create short notes")
    st.write("🎯 Solve practice questions")
    st.write("🔄 Revise important topics")

    st.success("Study plan generated!")

st.divider()

# ---------------- NOTES UPLOAD ----------------

st.header("Upload Notes")

uploaded_file = st.file_uploader(
    "Upload your notes",
    type=["pdf", "txt"]
)

text = ""

if uploaded_file:

    st.success("File uploaded successfully!")
    st.write("File Name:", uploaded_file.name)

    if uploaded_file.type == "text/plain":

        text = uploaded_file.read().decode("utf-8")

        st.subheader("Your Notes")
        st.text_area("Content", text, height=200)

    elif uploaded_file.type == "application/pdf":

        pdf = PdfReader(uploaded_file)

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        st.subheader("PDF Content")
        st.text_area("Content", text, height=200)

# ---------------- SUMMARY ----------------

if text:

    if st.button("Generate Summary"):

        sentences = text.split(".")

        st.subheader("Summary")

        for sentence in sentences[:5]:
            if sentence.strip():
                st.write("•", sentence.strip())

    st.divider()

    # ---------------- QUIZ ----------------

    if st.button("Generate Quiz"):

        st.subheader("Quiz")

        lines = text.split(".")

        count = 1

        for line in lines[:5]:

            line = line.strip()

            if len(line) > 10:

                words = line.split()

                if len(words) > 3:

                    question = " ".join(words[:-1])

                    st.write(f"Q{count}. Complete the statement:")

                    st.write(question + " ______")

                    with st.expander("Show Answer"):
                        st.write(words[-1])

                    count += 1