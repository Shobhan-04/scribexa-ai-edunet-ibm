from modules.gemini_utils import ask_gemini

def translate_notes(notes, language):

    prompt = f"""
    Translate the following notes
    into {language}

    Notes:

    {notes}
    """

    return ask_gemini(prompt)
  