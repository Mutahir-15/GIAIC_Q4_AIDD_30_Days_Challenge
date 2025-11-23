# quiz_generator.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz(text: str):
    prompt = f"""
    Using the following PDF text, generate a quiz with:

    - 10 MCQs
    - Each question must have 4 options
    - The question should be well formatted and easy to understand.
    - The answer should be in the format of a multiple choice question.
    - The answers options should be in the format of a multiple choice question.
    - Highlight the correct answer like this: **Correct Answer: X**

    PDF TEXT:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text
