from modules.groq_utils import ask_groq

def generate_flashcards(text):
    prompt = f"""Convert the following text into flashcards.
    Return ONLY JSON.
    
    Format:
    [
    {{"front":"Question",
    "back":"Answer"
    }}
    ]
    
    Text:
    {text}
    """

    response = ask_groq(prompt)
    return response
