import streamlit as st
import os

from modules.whisper_utils import transcribe_audio
from modules.image_processor import extract_text_from_image
from modules.pdf_processor import extract_text_from_pdf
from modules.youtube_processor import download_audio

from modules.content_generator import generate_study_material

from database.database import save_lecture
import json

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Scribexa AI | Turn Notes into Knowledge and Learn Faster. Remember Longer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Scribexa AI")

st.subheader("Turn Notes into Knowledge")

st.caption("Learn Faster. Remember Longer.")

# ---------------------------------------
# Create Upload Folder
# ---------------------------------------

os.makedirs("uploads", exist_ok=True)

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.header("Input Options")

option = st.sidebar.selectbox(
    "Select Input Type",
    [
        "Audio",
        "Image",
        "PDF",
        "YouTube"
    ]
)

youtube_url = ""

if option == "YouTube":

    youtube_url = st.text_input("Enter YouTube Lecture URL")

    if youtube_url:

        st.video(youtube_url)

        if st.button("Generate Study Material"):

            with st.spinner("Downloading lecture..."):

                audio_file = download_audio(youtube_url)

            with st.spinner("Transcribing..."):

                transcript = transcribe_audio(audio_file)

            result = generate_study_material(transcript)

            notes = result["notes"]

            flashcards = result["flashcards"]

            mcqs = result["mcqs"]

            st.success(
                "Study material generated!"
            )

# ---------------------------------------
# File Upload
# ---------------------------------------

uploaded_file = st.file_uploader(
    "Upload your file",
    type=None
)

# ---------------------------------------
# Variables
# ---------------------------------------

transcript = ""
notes = ""
flashcards = ""
mcqs = ""

# ---------------------------------------
# Processing
# ---------------------------------------

if uploaded_file:

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    try:

        # ---------------- AUDIO ----------------

        if option == "Audio":

            with st.spinner("🎙️ Transcribing audio..."):

                transcript = transcribe_audio(file_path)

        # ---------------- IMAGE ----------------

        elif option == "Image":

            with st.spinner("📝 Extracting handwritten text..."):

                transcript = extract_text_from_image(file_path)

        # ---------------- PDF ----------------

        elif option == "PDF":

            with st.spinner("📄 Reading PDF..."):

                transcript = extract_text_from_pdf(file_path)
        
        elif option == "YouTube":
            with st.spinner("Downloading lecture..."):
                audio_file = download_audio(youtube_url)
            with st.spinner("Transcribing lecture..."):
                transcript = transcribe_audio(audio_file)

        # ---------------- GENERATE CONTENT ----------------

        with st.spinner("🤖 Generating study material..."):

            result = generate_study_material(transcript)

            notes = result["notes"]

            flashcards = result["flashcards"]

            mcqs = result["mcqs"]

        # ---------------- DATABASE SAVE ----------------

        save_lecture(
            uploaded_file.name,
            transcript,
            str(notes),
            str(flashcards),
            str(mcqs)
        )

        st.success(
            "✅ Study materials generated successfully!"
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

# ---------------------------------------
# Results Section
# ---------------------------------------

if transcript:

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Transcript",
            "Notes",
            "Flashcards",
            "MCQs"
        ]
    )

  # Transcript
    with tab1:
        st.subheader("Transcript")
        st.text_area("Transcript",transcript, height=500)
        
   # Notes
    with tab2:
        st.subheader("Study Notes")
        st.markdown(notes)
    
    # Flashcards
    with tab3:
        st.subheader("Flashcards")
        
        for i, card in enumerate(flashcards):
            with st.expander(f"Flashcard {i+1}"):
                st.markdown("### Front")
                st.write(card["front"])
                
                st.markdown("### Back")
                st.write(card["back"])
    # MCQs
    with tab4:
        st.subheader("MCQs")

    try:

        for i, q in enumerate(mcqs):

            with st.expander(f"Question {i+1}"):

                st.write(q["question"])

                for opt in q["options"]:

                    st.write(f"- {opt}")

                st.success(
                    f"Answer: {q['answer']}"
                )

    except Exception as e:

        st.error(f"MCQ Display Error: {e}")

    # ---------------------------------------
    # Downloads
    # ---------------------------------------

    st.markdown("---")

    st.subheader("Downloads")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(
            label="📥 Download Notes",
            data=notes,
            file_name="notes.txt",
            mime="text/plain"
        )

    with col2:

        st.download_button(
            label="📥 Download Flashcards",
            data=flashcards,
            file_name="flashcards.txt",
            mime="text/plain"
        )

    with col3:

        st.download_button(
            label="📥 Download MCQs",
            data=mcqs,
            file_name="mcqs.txt",
            mime="text/plain"
        )
