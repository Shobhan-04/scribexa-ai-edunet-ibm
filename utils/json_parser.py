import json
import re

def extract_json(text: str):

    if not text:
        raise ValueError("Empty response")

    # Remove markdown code blocks
    text = text.replace("```json", "").replace("```", "").strip()

    # Extract first valid JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON found in response")

    json_str = match.group(0)

    try:
        return json.loads(json_str)
    except Exception as e:
        raise ValueError(f"JSON parse failed: {str(e)}\nRAW:\n{text}")
