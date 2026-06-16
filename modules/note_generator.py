from modules.gemini_utils import ask_gemini

def generate_notes(text):

    prompt = f"""
    Convert the following lecture transcript into
    well-structured study notes.

    Transcript:
    {text}
    """

    return ask_gemini(prompt)