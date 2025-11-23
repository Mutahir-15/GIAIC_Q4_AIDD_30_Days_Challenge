# agent.py
from extractor import extract_pdf_text
from summarizer import generate_summary
from quiz_generator import generate_quiz

class PDFQuizAgent:

    def process_pdf(self, file):
        return extract_pdf_text(file)

    def summarize(self, text):
        return generate_summary(text)

    def quiz(self, text):
        return generate_quiz(text)
