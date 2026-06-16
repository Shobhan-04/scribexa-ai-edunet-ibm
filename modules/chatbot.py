import streamlit as st
from modules.gemini_utils import ask_gemini

def ask_notes_question(notes, question):

    prompt = f"""
    Answer only from these notes.

    Notes:
    {notes}

    Question:
    {question}
    """

    return ask_gemini(prompt)
  
# Streamlit
question = st.text_input(
    "Ask Questions"
)

if question:

    answer = ask_notes_question(
        notes,
        question
    )

    st.write(answer)