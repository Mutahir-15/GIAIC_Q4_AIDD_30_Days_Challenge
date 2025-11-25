from agent.extractor import extract_text_from_pdf
from agent.summarizer import summarize_text
from agent.quiz_generator import generate_mcq_quiz, generate_mixed_quiz

class PdfAgent:
    def __init__(self):
        self.original_text = None

    def process_pdf(self, pdf_file):
        """
        Extracts text from the PDF and stores it.
        """
        self.original_text = extract_text_from_pdf(pdf_file)
        return self.original_text

    def get_summary(self):
        """
        Generates a summary of the stored text.
        """
        if not self.original_text:
            return "Please process a PDF first."
        return summarize_text(self.original_text)

    def create_quiz(self, quiz_type="mcq", num_questions=10):
        """
        Generates a quiz from the stored text.
        """
        if not self.original_text:
            return "Please process a PDF first."
        
        if quiz_type == "mcq":
            return generate_mcq_quiz(self.original_text, num_questions)
        elif quiz_type == "mixed":
            return generate_mixed_quiz(self.original_text, num_questions)
        else:
            return "Invalid quiz type specified."
