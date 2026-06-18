import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def ask_hf(prompt):

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 800,
                    "temperature": 0.7
                }
            }
        )

        result = response.json()

        # Hugging Face sometimes returns list
        if isinstance(result, list):
            return result[0]["generated_text"]

        return result

    except Exception as e:
        return f"ERROR: {str(e)}"
