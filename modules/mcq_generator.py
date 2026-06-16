from modules.gemini_utils import ask_gemini

def generate_mcqs(text):

    prompt = f"""
    You are an expert teacher.

    Generate 10 MCQs from the following content.

    For each MCQ provide:

    Question
    A
    B
    C
    D
    Correct Answer

    Content:

    {text}
    """

    return ask_gemini(prompt)