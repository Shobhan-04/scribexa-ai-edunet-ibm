from modules.hf_utils import ask_hf

def generate_notes(text):

    prompt = f"""
    Convert the following lecture transcript into
    well-structured study notes.

    Transcript:
    {text}
    """

    return ask_hf(prompt)
