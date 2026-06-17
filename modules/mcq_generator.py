from modules.gemini_utils import ask_gemini

def generate_mcqs(text):

    prompt = f"""
    Generate 10 MCQs from the text.

    Return ONLY valid JSON.

    Format:

    [
      {{
        "question":"Question",
        "options":["A","B","C","D"],
        "answer":"Correct Answer"
      }}
    ]

    Text:
    {text}
    """

    return ask_gemini(prompt)
