from modules.hf_utils import ask_hf
import json

def generate_study_material(text):

    text = text[:4000]

    prompt = f"""
Generate study material in JSON format:

{{
  "notes":"...",
  "flashcards":[{{"front":"...","back":"..."}}],
  "mcqs":[{{"question":"...","options":["A","B","C","D"],"answer":"..."}}]
}}

TEXT:
{text}
"""

    response = ask_hf(prompt)

    import re
    import json

    match = re.search(r"\{.*\}", response, re.DOTALL)
    if match:
        response = match.group(0)

    return json.loads(response)
