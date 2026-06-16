# 📚 Scribexa AI

### Turn Notes into Knowledge

**Learn Faster. Remember Longer.**

AI-Powered Lecture-to-Notes Generator using Speech Recognition, OCR, NLP, and Generative AI. Upload lectures, PDFs, or handwritten notes and instantly generate AI-powered notes, flashcards, quizzes, and revision materials.

## Overview

Scribexa AI helps students convert lecture recordings, handwritten notes, and PDFs into structured study materials.

The platform automatically generates:

* Lecture Transcripts
* Study Notes
* Flashcards
* Multiple Choice Questions (MCQs)

This eliminates the need for manual note-taking and improves revision efficiency.

---

## Features

### 🎙 Audio to Notes

* Upload MP3/WAV lecture recordings
* Automatic speech-to-text using Whisper

### 📝 Handwritten Notes OCR

* Upload handwritten notes
* AI-powered text extraction using Gemini Vision

### 📄 PDF Processing

* Extract text from PDFs
* Generate study materials automatically

### 🤖 AI Study Material Generation

* Detailed Notes
* Key Points
* Flashcards
* MCQs

### 💾 Database Storage

* Store generated content using SQLite

### 📥 Download Support

* Download Notes
* Download Flashcards
* Download MCQs

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Models

* Whisper
* Google Gemini

### Database

* SQLite

### Libraries

* streamlit
* google-generativeai
* python-dotenv
* openai-whisper
* pillow
* pymupdf
* fpdf2
* sqlite3

---

## Project Structure

```text
ScribexaAI/

├── app.py
├── requirements.txt
├── .env

├── modules/
│   ├── whisper_utils.py
│   ├── gemini_utils.py
│   ├── image_processor.py
│   ├── pdf_processor.py
│   ├── note_generator.py
│   ├── flashcard_generator.py
│   ├── mcq_generator.py
│   └── pdf_export.py

├── database/
│   ├── database.py
│   └── scribexa.db

├── uploads/
├── outputs/

└── notebooks/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ScribexaAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## Gemini API Setup

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your Gemini API key from Google AI Studio.

---

## Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* AI Chat Assistant
* Revision Notes Generator
* Exam Question Predictor
* YouTube Lecture Support
* Multi-Language Notes
* Mind Map Generation
* Cloud Deployment

---

## Author

Shobhan Satpathy

Computer Science Student | AI/ML Enthusiast | Full Stack Web Developer
