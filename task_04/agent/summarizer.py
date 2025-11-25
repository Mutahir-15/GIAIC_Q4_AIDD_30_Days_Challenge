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


def summarize_text(text, model_name="gemini-2.5-flash"):
    """
    Generates a summary of the given text using the Gemini model.

    Args:
        text: The text to be summarized.
        model_name: The name of the Gemini model to use.

    Returns:
        A string containing the generated summary.
    """

    if not text:
        return "No text provided to summarize."

    model = genai.GenerativeModel(model_name)
    prompt = f"Please provide a concise summary of the following text:\n\n{text}"

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred during summarization: {e}"

