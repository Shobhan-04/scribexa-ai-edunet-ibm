from modules.gemini_utils import ask_gemini
def generate_notes(text):

    prompt = f"""
    Generate:
    1 Summary
    2 Key Points
    3 Detailed Notes

    Text:

    {text}
    """

    return ask_gemini(prompt)