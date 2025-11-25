import streamlit as st
from agent.agent import PdfAgent

st.set_page_config(page_title="PDF Summarizer & Quiz Generator", layout="wide")

def main():
    st.title("📄 PDF Summarizer & Quiz Generator")

    # Initialize agent in session state
    if "agent" not in st.session_state:
        st.session_state.agent = PdfAgent()
    
    # Initialize messages list in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # File uploader
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

    if uploaded_file:
        with st.spinner("Processing PDF..."):
            agent = st.session_state.agent
            extracted_text = agent.process_pdf(uploaded_file)
            if "Error" in extracted_text:
                st.error(extracted_text)
            else:
                st.success("PDF processed successfully!")
                st.session_state.messages.append({"role": "assistant", "content": "PDF processed. Ready to summarize or generate a quiz."})


    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Summary"):
            if st.session_state.agent.original_text:
                with st.spinner("Generating summary..."):
                    summary = st.session_state.agent.get_summary()
                    st.session_state.messages.append({"role": "assistant", "content": f"**Summary:**\n{summary}"})
                    st.rerun()
            else:
                st.warning("Please upload a PDF first.")

    with col2:
        quiz_type = st.selectbox("Select Quiz Type", ["mcq", "mixed"], key="quiz_type")
        if st.button("Create Quiz"):
            if st.session_state.agent.original_text:
                with st.spinner("Creating quiz..."):
                    quiz = st.session_state.agent.create_quiz(quiz_type=st.session_state.quiz_type)
                    st.session_state.messages.append({"role": "assistant", "content": f"**{quiz_type.upper()} Quiz:**\n{quiz}"})
                    st.rerun()

            else:
                st.warning("Please upload a PDF first.")


if __name__ == "__main__":
    main()
