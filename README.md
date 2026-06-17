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
## 🚀 Live Demo

Streamlit App:
(https://scribexa-ai-edunet-ibm.streamlit.app/)

Landing Page : 
(https://scribexa-ai-landing-page.lovable.app/)

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

### 🎥 YouTube Lecture Processing

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

## 🛠 Tech Stack

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

### 🏗 Architecture Diagram 
```
User
   │
   ▼
Streamlit Web Application
   │
   ├── Audio Upload
   ├── PDF Upload
   ├── Image Upload
   └── YouTube URL
            │
            ▼
      Processing Layer
   ├── Whisper (Speech-to-Text)
   ├── PyMuPDF (PDF Extraction)
   ├── OCR (Image Text Extraction)
   └── yt-dlp (YouTube Audio Download)
            │
            ▼
      Gemini AI Engine
            │
            ▼
   ├── Study Notes
   ├── Flashcards
   ├── MCQs
   ├── Revision Notes
   └── AI Chat Assistant
            │
            ▼
      SQLite Database
            │
            ▼
      Export & Download
   ├── PDF Export
   ├── Notes Download
   ├── Flashcards Download
   └── MCQs Download
            │
            ▼
      Streamlit Cloud
```

---

## 📂 Project Structure

```
scribexa-ai-edunet-ibm/
│
├── app.py
├── requirements.txt
├── packages.txt
├── runtime.txt
├── .gitignore
├── README.md
│
├── assets/
│   ├── home.png
│   ├── upload.png
│   ├── notes.png
│   ├── flashcards.png
│   ├── mcqs.png
│
├── modules/
│   ├── **init**.py
│   │
│   ├── whisper_utils.py
│   ├── gemini_utils.py
│   ├── pdf_processor.py
│   ├── image_processor.py
│   ├── youtube_processor.py
│   ├── content_generator.py
│   ├── note_generator.py
│   ├── flashcard_generator.py
│   ├── mcq_generator.py
│   ├── revision_generator.py
│   ├── chatbot.py
│   ├── exam_predictor.py
│   ├── translator.py
│   └── pdf_export.py
│
├── database/
│   ├── database.py
│   └── scribexa.db
│
├── notebooks/
│   ├── Phase1_Whisper_Test.ipynb
│   ├── Phase2_Gemini_Test.ipynb
│   ├── Phase3_Notes_Test.ipynb
│   ├── Phase4_Flashcards.ipynb
│   ├── Phase5_MCQ_Test.ipynb
│   ├── Phase6_OCR_Test.ipynb
│   ├── Phase7_PDF_Processing.ipynb
│   ├── Phase8_PDF_Export.ipynb
│
├── docs/
│   ├── Presentation.pptx
│
├── .streamlit/
│ ├── config.toml
│ └── secrets.toml # Local only
```

---

## 📷 Screenshots

---
## Installation

### Clone Repository

```bash
git clone (https://github.com/Shobhan-04/scribexa-ai-edunet-ibm.git)
cd scribexa-ai-edunet-ibm
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

## ⚠ Known Limitations
Uses Gemini Free Tier API.
API requests are subject to daily and rate limits.
If quota is exceeded, content generation may be temporarily unavailable until the quota resets.
---
## 🔮Future Enhancements

* AI Chat Assistant
* Revision Notes Generator
* Exam Question Predictor
* Multi-Language Support
* Mind Map Generation
* Cloud Deployment
* RAG-based Study Assistant

---

## 👨‍💻 Author

Shobhan Satpathy

Computer Science Student | AI/ML Enthusiast | Full Stack Web Developer
GitHub:
(https://github.com/Shobhan-04)

LinkedIn:
(www.linkedin.com/in/shobhanengineer)

⭐ If you found this project useful, please star the repository.

---

## 📜 License

This project is developed for educational and learning purposes.
