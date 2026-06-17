import json
import re
from modules.groq_utils import ask_groq

def generate_study_material(text):

    text = text[:4000]  # reduce load

    prompt = f"""
    Generate study material.
    Return ONLY valid JSON.
    
    {{
    "notes":"...",
    "flashcards":[{{"front":"...","back":"..."}}],
    "mcqs":[{{"question":"...","options":["A","B","C","D"],"answer":"..."}}]
    }}
    
    TEXT: 
    {text}
    """

    try:
        response = ask_groq(prompt)

        if not response:
            raise Exception("Empty response from Groq")

        # extract JSON safely
        match = re.search(r"\{.*\}", response, re.DOTALL)
        if match:
            response = match.group(0)

        data = json.loads(response)

        return data

    except Exception as e:
        print("GENERATION ERROR:", str(e))
        return {
            "notes": "⚠️ Generation failed (API/Quota/Parsing error)",
            "flashcards": [],
            "mcqs": []
        }
