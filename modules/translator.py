from modules.hf_utils import ask_hf

def translate_notes(notes, language):

    prompt = f"""
    Translate the following notes
    into {language}

    Notes:

    {notes}
    """

    return ask_hf(prompt)
  
