import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def ask_llm(prompt):

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 800,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"HF Error: {response.text}")

    result = response.json()

    # HF sometimes returns list
    if isinstance(result, list):
        return result[0].get("generated_text", "")

    return result.get("generated_text", "")
