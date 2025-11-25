import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# Configure the Gemini API key
api_key = (
    os.getenv("GEMINI_API_KEY")      # used in your day-by-day tasks
    or os.getenv("GOOGLE_API_KEY")   # required by official SDK
)

if not api_key:
    raise ValueError(
        "❌ No API Key found!\n"
        "Please set either GEMINI_API_KEY or GOOGLE_API_KEY in your .env file."
    )

# Configure the Gemini client
genai.configure(api_key=api_key)

def generate_mcq_quiz(text, num_questions=10, model_name="gemini-2.5-flash"):
    """
    Generates a multiple-choice quiz from the given text using the Gemini model.

    Args:
        text: The text to generate the quiz from.
        num_questions: The number of questions to generate.
        model_name: The name of the Gemini model to use.

    Returns:
        A string containing the generated quiz.
    """
    if not text:
        return "No text provided to generate a quiz from."

    model = genai.GenerativeModel(model_name)
    prompt = f"""
    Based on the following text, generate a multiple-choice quiz with {num_questions} questions.
    Each question should have 4 options, and the correct answer must be clearly indicated.
    Format the output cleanly.

    Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred during quiz generation: {e}"

def generate_mixed_quiz(text, num_questions=10, model_name="gemini-2.5-flash"):
    """
    Generates a mixed-style quiz from the given text using the Gemini model.

    Args:
        text: The text to generate the quiz from.
        num_questions: The number of questions to generate.
        model_name: The name of the Gemini model to use.

    Returns:
        A string containing the generated quiz.
    """
    if not text:
        return "No text provided to generate a quiz from."

    model = genai.GenerativeModel(model_name)
    prompt = f"""
    Based on the following text, generate a mixed-style quiz with {num_questions} questions.
    This can include multiple-choice, fill-in-the-blank, and short-answer questions.
    The correct answers must be provided.
    Format the output cleanly.

    Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred during quiz generation: {e}"
