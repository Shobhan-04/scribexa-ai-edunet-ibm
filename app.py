import streamlit as st
import os

from modules.whisper_utils import transcribe_audio
from modules.image_processor import extract_text_from_image
from modules.pdf_processor import extract_text_from_pdf

from modules.note_generator import generate_notes
from modules.flashcard_generator import generate_flashcards
from modules.mcq_generator import generate_mcqs

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
        "PDF"
    ]
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

        # ---------------- GENERATE CONTENT ----------------

        with st.spinner(
            "🤖 Generating study material..."
        ):

            notes = generate_notes(transcript)

            flashcards = generate_flashcards(transcript)

            mcqs = generate_mcqs(transcript)

        # ---------------- DATABASE SAVE ----------------

        save_lecture(
            uploaded_file.name,
            transcript,
            notes,
            flashcards,
            mcqs
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

        st.subheader(
            "Transcript"
        )

        st.write(transcript)

    # Notes

    with tab2:

        st.subheader(
            "Study Notes"
        )

        st.write(notes)

    # Flashcards

    with tab3:

        st.subheader(
            "Flashcards"
        )
        
        flashcards_data = json.loads(flashcards)
        
        for i, card in enumerate(flashcards_data):
            with st.expander(f"Flashcard {i+1}"):
                st.markdown(f"**Q:** {card['front']}")
                st.markdown(f"**A:** {card['back']}")
    # MCQs

    with tab4:

        st.subheader(
            "MCQs"
        )

        st.write(mcqs)

    # ---------------------------------------
    # Downloads
    # ---------------------------------------

    st.markdown("---")

    st.subheader(
        "Downloads"
    )

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
