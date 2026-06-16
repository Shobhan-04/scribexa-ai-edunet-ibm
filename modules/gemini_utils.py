import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API Key not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text