from modules.hf_utils import ask_hf

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

    return ask_hf(prompt)
