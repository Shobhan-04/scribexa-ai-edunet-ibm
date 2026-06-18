import json
import re

def extract_json(text: str):

    if not text:
        raise ValueError("Empty response from model")

    text = text.replace("```json", "").replace("```", "").strip()

    # Try direct parsing first
    try:
        return json.loads(text)
    except:
        pass

    # Try extracting JSON block
    match = re.search(r"\{[\s\S]*\}", text)

    if match:
        try:
            return json.loads(match.group())
        except:
            raise ValueError(f"Invalid JSON structure:\n{text}")

    raise ValueError(f"No JSON found in response:\n{text}")
