import json
import re
from modules.groq_utils import ask_groq

def generate_study_material(text):

    # Prevent huge prompts
    text = text[:10000]

    prompt = f"""
Generate study material from the following text.

Return ONLY valid JSON.

{{
    "notes":"Detailed study notes",

    "flashcards":[
        {{
            "front":"Question",
            "back":"Answer"
        }}
    ],

    "mcqs":[
        {{
            "question":"Question",
            "options":["A","B","C","D"],
            "answer":"Correct Answer"
        }}
    ]
}}

TEXT:
{text}
"""

    print("Sending to Groq...")
    print("TEXT LENGTH:", len(text))
    
    response = ask_groq(prompt)
    
    print("Groq response received")
    print("RAW GROQ RESPONSE:")
    print(response)

    match = re.search(r"\{.*\}", response, re.DOTALL)
    
    if match:
        response = match.group(0)

    try:
        response = ask_groq(prompt)
        if response.startswith("ERROR"):
            raise Exception(response)
            return json.loads(response)
    
    except Exception as e:
        print("RAW GROQ RESPONSE:")
        print(response)
        raise Exception(f"Groq returned invalid JSON: {e}")
