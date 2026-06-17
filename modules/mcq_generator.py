from modules.gemini_utils import ask_gemini

def generate_mcqs(text):
    prompt = f"""
    Create 5 multiple choice questions from the text.

    Return ONLY JSON:
    [
      {
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "answer": "A"
      }
    ]

    Text:
    {text}
    """

    return ask_gemini(prompt)
