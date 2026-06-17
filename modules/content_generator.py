import json
from modules.groq_utils import ask_groq

def generate_study_material(text):

    text = text[:12000]
    prompt = f"""You are an educational assistant.
    Analyze the lecture content.
    Return ONLY valid JSON.
    
    Do not write explanations.
    Do not use markdown.
    Do not use ```json blocks.
    
    JSON schema:
    {{
    "notes": "string",
    
    "flashcards": [
    {{
    "front": "string",
    "back": "string"
    }}
    ],
    
    "mcqs": [
    {{
    "question": "string",
    "options": [
    "A",
    "B",
    "C",
    "D"
    ],
    answer": "string"
    }}
    ]
    }}
    
    Generate:
    concise study notes
    - 10 flashcards
    - 10 MCQs
    
    Lecture Text:
    {text}
    """
    response = ask_groq(prompt)
    if not response:
        raise Exception("Groq returned an empty response.")

    if response.startswith("ERROR:"):
        raise Exception(response)

    response = response.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()

    try:
        return json.loads(response)

    except Exception as e:
        raise Exception(f"""Groq returned invalid JSON.
        Response received: {response}
        Error: {str(e)}
        """
    )
