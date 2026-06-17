import streamlit as st
import os

from modules.whisper_utils import transcribe_audio
from modules.image_processor import extract_text_from_image
from modules.pdf_processor import extract_text_from_pdf
from modules.youtube_processor import download_audio
from modules.chatbot import chatbot_ui 

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

if uploaded_file or (
    option == "YouTube" and youtube_url
):

    try:

        transcript = ""

        # ---------------- AUDIO ----------------

        if option == "Audio":

            file_path = os.path.join(
                "uploads",
                uploaded_file.name
            )

            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            with st.spinner(
                "🎙️ Transcribing audio..."
            ):
                transcript = transcribe_audio(file_path)

        # ---------------- IMAGE ----------------

        elif option == "Image":

            file_path = os.path.join(
                "uploads",
                uploaded_file.name
            )

            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            with st.spinner(
                "📝 Extracting handwritten text..."
            ):
                transcript = extract_text_from_image(file_path)

        # ---------------- PDF ----------------

        elif option == "PDF":

            file_path = os.path.join(
                "uploads",
                uploaded_file.name
            )

            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            with st.spinner(
                "📄 Reading PDF..."
            ):
                transcript = extract_text_from_pdf(file_path)

        # ---------------- YOUTUBE ----------------

        elif option == "YouTube":

            with st.spinner(
                "📥 Downloading lecture..."
            ):
                audio_file = download_audio(
                    youtube_url
                )

            with st.spinner(
                "🎙️ Transcribing lecture..."
            ):
                transcript = transcribe_audio(
                    audio_file
                )

        # ---------------- VALIDATION ----------------

        if not transcript.strip():

            st.error(
                "No text extracted."
            )

            st.stop()

        # ---------------- GENERATE CONTENT ----------------

        with st.spinner(
            "🤖 Generating study material..."
        ):

            result = generate_study_material(
                transcript
            )

            notes = result["notes"]

            flashcards = result["flashcards"]

            mcqs = result["mcqs"]

        # ---------------- DATABASE ----------------

        filename = (
            uploaded_file.name
            if uploaded_file
            else youtube_url
        )

        save_lecture(
            filename,
            transcript,
            json.dumps(notes),
            json.dumps(flashcards),
            json.dumps(mcqs)
        )

        st.success(
            "✅ Study materials generated successfully!"
        )

    except Exception as e:

        if "429" in str(e):

            st.warning(
                """
                Gemini free quota exceeded.

                Please wait a few minutes
                and try again.
                """
            )

        else:

            st.error(str(e))
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

    st.subheader(
        "Flashcards"
    )

    for i, card in enumerate(
        flashcards
    ):

        with st.expander(
            f"Flashcard {i+1}"
        ):

            st.write(
                card["front"]
            )

            st.success(
                card["back"]
            )
            
    # MCQs
   with tab4:

    st.subheader("MCQs")

    for i, q in enumerate(mcqs):

        with st.expander(f"Question {i+1}"):

            st.write(q["question"])

            for opt in q["options"]:

                st.write(f"• {opt}")

            st.success(f"Answer: {q['answer']}")

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
