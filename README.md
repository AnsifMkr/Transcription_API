# 🎙️ YouTube Audio Transcriber API

This Django-based API extracts and transcribes audio from a YouTube video or short link provided in a POST request.

---

## 🚀 Features

- Accepts YouTube links (including Shorts)
- Downloads audio and generates transcript
- Simple API endpoint

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

# 🎙️ YouTube Audio Transcriber API

This Django-based API extracts and transcribes audio from a YouTube video or short link provided in a POST request.

---

## 🚀 Features

- Accepts YouTube links (including Shorts)
- Downloads audio and generates transcript
- Simple API endpoint

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Start the Development Server
python manage.py runserver


Now open your browser and go to:
http://127.0.0.1:8000/

## API 
### POST /api/transcript/
**URL:**  
`http://127.0.0.1:8000/api/transcript/`

**Content-Type:**  
`application/json`

**Payload (Body):**
```json
{
  "link_audio": "https://youtube.com/shorts/4DrO-dVAEgk?si=6EH9_5jSXyAwnpUf"
}
```




