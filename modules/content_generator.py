from modules.llm_router import ask_llm
from utils.json_parser import extract_json

def generate_study_material(text):

    text = text[:4000]

    prompt = f"""
You are an AI that returns ONLY valid JSON.

Generate:
- notes
- 10 flashcards
- 10 MCQs

Return format:

{{
  "notes": "...",
  "flashcards": [
    {{"front":"...","back":"..."}}
  ],
  "mcqs": [
    {{
      "question":"...",
      "options":["A","B","C","D"],
      "answer":"..."
    }}
  ]
}}

TEXT:
{text}
"""

    response = ask_llm(prompt)

    return extract_json(response)

    import re
    import json

    match = re.search(r"\{.*\}", response, re.DOTALL)
    if match:
        response = match.group(0)

    return json.loads(response)
