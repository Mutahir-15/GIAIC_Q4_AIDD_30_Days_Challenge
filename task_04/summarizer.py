# summarizer.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_summary(text: str):
    prompt = f"""
    Summarize the following PDF content into clean, meaningful, short paragraphs.

    PDF CONTENT:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
