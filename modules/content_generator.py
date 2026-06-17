import json
from modules.gemini_utils import ask_gemini

def generate_study_material(text):

    prompt = f"""
   You are an expert educational tutor.
   
   Analyze the lecture transcript and create:
   
   1. Structured Study Notes
   2. Important Key Concepts
   3. 10 Flashcards
   4. 10 MCQs
   
   Make notes concise and exam-oriented.
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
