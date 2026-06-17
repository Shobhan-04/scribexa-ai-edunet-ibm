import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Try .env first
api_key = os.getenv("GROQ_API_KEY")

# Streamlit Cloud fallback
if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

client = Groq(
    api_key=api_key
)

def ask_groq(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
