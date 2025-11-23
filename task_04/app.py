# app.py
import streamlit as st
from agent import PDFQuizAgent

agent = PDFQuizAgent()

st.title("📘 PDF Summarizer + Quiz Generator (Gemini Version)")

uploaded = st.file_uploader("Upload a PDF", type="pdf")

if uploaded:
    pdf_text = agent.process_pdf(uploaded)
    st.success("PDF loaded successfully!")

    if st.button("Generate Summary"):
        summary = agent.summarize(pdf_text)
        st.subheader("📄 Summary")
        st.write(summary)

        st.session_state["pdf_text"] = pdf_text

    if "pdf_text" in st.session_state:
        if st.button("Create Quiz"):
            quiz = agent.quiz(st.session_state["pdf_text"])
            st.subheader("📝 Quiz")
            st.write(quiz)
