import json
import re

def extract_json(text: str):

    if not text:
        return None  

    text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)
    except:
        pass

    match = re.search(r"\{[\s\S]*\}", text)

    if match:
        try:
            return json.loads(match.group())
        except:
            return None  

    return None
