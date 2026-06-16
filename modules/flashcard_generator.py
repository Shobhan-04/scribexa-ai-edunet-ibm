
# Create Module

from modules.gemini_utils import ask_gemini
def generate_flashcards(text):

    prompt = f"""
    Generate 10 flashcards.

    Text:

    {text}
    """

    return ask_gemini(prompt)