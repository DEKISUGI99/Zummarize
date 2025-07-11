# 🎥 Zummarize - YouTube Video Summarizer Extension

Zummarize is a **Chrome extension** that helps you **quickly understand long YouTube videos** by generating concise, meaningful summaries of their transcripts using advanced NLP models.

## 🔍 Features

- 🧠 AI-powered summarization using Hugging Face transformers (BART)
- 🧩 Intelligent chunking and deduplication of transcript
- 🎯 Topic-based or clean summarization (configurable)
- ⚙️ Extension icon click opens summary in a new tab
- 🖥️ Simple, readable UI with spinner and formatting

---

## 🚀 How It Works

1. The extension detects a YouTube video when clicked.
2. It extracts the video ID and sends it to a Flask backend.
3. The backend:
   - Downloads the transcript using `yt-dlp`
   - Chunks and summarizes it using the `facebook/bart-large-cnn` model
4. The summary is displayed on a clean webpage for the user.

---

## 📁 Project Structure

Zummarize/
│
├── extension/
│ ├── manifest.json
│ ├── summary.html
│ ├── summary.js
│ ├── style.css
│ └── icon.png
│
├── backend/
│ ├── app.py
│ ├── summary.py
│ └── requirements.txt
│
└── README.md


---

## 🛠️ Installation

### 🧩 Load the Extension

1. Go to `chrome://extensions`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the `extension/` folder

### 🐍 Set Up the Backend

1. Navigate to the `backend/` folder.
2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows


pip install -r requirements.txt
python app.py

This project is open source under the [MIT License](./LICENSE).
