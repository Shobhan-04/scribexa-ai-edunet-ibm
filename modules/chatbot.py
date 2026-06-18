import streamlit as st
from modules.hf_utils import ask_hf

def ask_notes_question(notes, question):

    prompt = f"""
    Answer ONLY using the information present in these notes.

    Notes:
    {notes}

    Question:
    {question}
    """

    return ask_hf(prompt)


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
