from modules.llm_router import ask_llm
from utils.json_parser import extract_json
import re


def clean_text(text):
    text = text[:3000] 
    text = re.sub(r'\s+', ' ', text)  
    return text.strip()

def generate_study_material(text):

    text = clean_text(text)

    prompt = f"""
You are an expert JSON generator.

STRICT RULES:
- Output ONLY valid JSON
- No explanation
- No markdown
- No extra text before or after JSON

If you cannot comply, output:
{{"error":"invalid"}}

FORMAT:
{{
  "notes": "short structured notes",
  "flashcards": [
    {{"front": "Q", "back": "A"}}
  ],
  "mcqs": [
    {{
      "question": "Q",
      "options": ["A","B","C","D"],
      "answer": "A"
    }}
  ]
}}

TEXT:
{text}
"""
    response = ask_llm(prompt)

    if not response or len(response.strip()) < 30:
        response = ask_llm(prompt)

    if not response or len(response.strip()) < 30:
        raise Exception("AI failed to generate valid response")

    try:
        data = extract_json(response)

        if not data:
            raise Exception("Empty JSON after parsing")

        return data

    except Exception:
       
        fix_prompt = f"""
Fix this into VALID JSON ONLY.

Return ONLY JSON.

CONTENT:
{response}
"""

        response2 = ask_llm(fix_prompt)

        data = extract_json(response2)

        if not data:
            raise Exception("Failed even after repair attempt")

        return data
