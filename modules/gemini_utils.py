import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Streamlit Cloud fallback
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        raise ValueError(
            "Gemini API Key not found in .env or Streamlit Secrets"
        )

genai.configure(api_key=api_key)

print("MODEL LOADED: gemini-2.5-flash")

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("GEMINI ERROR:")
        print(str(e))
        return f"ERROR: {str(e)}"
