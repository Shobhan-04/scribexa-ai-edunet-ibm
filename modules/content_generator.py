import json
from modules.gemini_utils import ask_gemini

def generate_study_material(text):

    prompt = f"""
    From the following lecture text generate:

    1. Structured Study Notes
    2. 10 Flashcards
    3. 10 MCQs

    Return ONLY valid JSON.

    Format:

    {{
        "notes": "study notes here",

        "flashcards": [
            {{
                "front": "question",
                "back": "answer"
            }}
        ],

        "mcqs": [
            {{
                "question": "question",
                "options": [
                    "option1",
                    "option2",
                    "option3",
                    "option4"
                ],
                "answer": "correct answer"
            }}
        ]
    }}

    Lecture Text:

    {text}
    """

    response = ask_gemini(prompt)

    return json.loads(response)
