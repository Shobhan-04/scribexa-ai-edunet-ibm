from modules.llm_router import ask_llm
from utils.json_parser import extract_json

def generate_study_material(text):

    text = text[:4000]

    prompt = f"""
    You are a STRICT JSON generator.
    
    RULES:
    - Return ONLY valid JSON
    - No explanation
    - No markdown
    - No text before or after JSON
    
    Output format:
    {{
    "notes": "string",
    "flashcards": [
    {{"front": "string", "back": "string"}}
    ],
    "mcqs": [
    {{
    "question": "string",
    "options": ["A","B","C","D"],
    "answer": "string"
    }}
    ]
    }}
    
    TEXT:
    {text}
    """

    response = ask_hf(prompt)
    
    try:
        return extract_json(response)
    
    except Exception:
        fix_prompt = f"""
        Fix this into VALID JSON ONLY:
        {response}
        Return ONLY JSON.
        """
        
        response2 = ask_hf(fix_prompt)
        return extract_json(response2)
