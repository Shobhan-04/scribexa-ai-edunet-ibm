import json
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

    response = ask_groq(prompt)

    response = response.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    ).strip()

    return json.loads(response)
