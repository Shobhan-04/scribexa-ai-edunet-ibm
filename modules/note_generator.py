from modules.groq_utils import ask_groq

def generate_notes(text):

    prompt = f"""
    Convert the following lecture transcript into
    well-structured study notes.

    Transcript:
    {text}
    """

    return ask_groq(prompt)
