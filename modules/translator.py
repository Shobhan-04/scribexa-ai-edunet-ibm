from modules.groq_utils import ask_groq

def translate_notes(notes, language):

    prompt = f"""
    Translate the following notes
    into {language}

    Notes:

    {notes}
    """

    return ask_groq(prompt)
  
