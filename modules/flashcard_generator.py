from modules.gemini_utils import ask_gemini

def generate_flashcards(text):
    prompt = f"""
    Convert the following text into flashcards.

    Return ONLY JSON in this format:
    [
      {"front": "question", "back": "answer"},
      ...
    ]

    Text:
    {text}
    """

    response = ask_gemini(prompt)
    return response
