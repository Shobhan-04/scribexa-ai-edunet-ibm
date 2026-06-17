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
      "notes":"...",
      "flashcards":[
        {{
          "front":"...",
          "back":"..."
        }}
      ],
      "mcqs":[
        {{
          "question":"...",
          "options":["A","B","C","D"],
          "answer":"..."
        }}
      ]
    }}

    Lecture Text:

    {text}
    """

    response = ask_gemini(prompt)
    print("========== GEMINI RESPONSE ==========")
    print(response)
    print("====================================")

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
        raise Exception(f"""Gemini returned invalid JSON.
        Response received: {response}
        Error: {str(e)}
        """
    )
