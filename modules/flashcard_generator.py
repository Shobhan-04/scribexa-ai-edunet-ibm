from modules.hf_utils import ask_hf

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

    response = ask_hf(prompt)
    return response
