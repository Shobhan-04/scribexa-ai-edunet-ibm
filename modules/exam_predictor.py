from modules.gemini_utils import ask_gemini

def predict_exam_questions(
    text
):

    prompt = f"""
    Generate the 10 most likely
    university exam questions.

    Content:

    {text}
    """

    return ask_gemini(prompt)