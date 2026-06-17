import streamlit as st
from modules.groq_utils import ask_groq

def ask_notes_question(notes, question):

    prompt = f"""
    Answer ONLY using the information present in these notes.

    Notes:
    {notes}

    Question:
    {question}
    """

    return ask_groq(prompt)


def chatbot_ui(notes):

    st.subheader("🤖 AI Study Assistant")

    question = st.text_input(
        "Ask a question about your notes"
    )

    if question:

        answer = ask_notes_question(
            notes,
            question
        )

        st.success(answer)
