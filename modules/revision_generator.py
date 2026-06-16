from modules.gemini_utils import ask_gemini

def generate_revision_notes(
    text
):

    prompt = f"""
    Create a one-page exam revision sheet.

    Include:

    Key Concepts
    Definitions
    Formulas
    Important Points

    Content:

    {text}
    """

    return ask_gemini(prompt)