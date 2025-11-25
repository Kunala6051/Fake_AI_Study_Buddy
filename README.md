Moodio — AI-Based Adaptive Learning & Emotion-Aware Study Assistant

Moodio is an AI-powered web application that generates personalized study plans, tracks progress, provides quizzes, and adapts to user emotions using real-time webcam detection.

🚀 Features

AI-Generated Study Plans using Google Gemini API

Emotion Detection with OpenCV + Haar Cascade

Interactive Dashboard & Roadmaps

On-Demand Quiz Generator

Progress Tracking & Analytics

MongoDB Storage for flexible JSON data

Conversational Chatbot for study help

🧰 Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Django (Python)


AI: Google Gemini API, OpenCV, NumPy


Database: MongoDB

📂 Folder Structure

```
Moodio/
│── manage.py
│── db.sqlite3
│── quiz_history.json
│── users.json
│── result.json
│
├── Moodio/          # Django project (settings, urls, wsgi/asgi)
│
└── chatbot/         # Main app (views, models, templates, static)
```

⚙️ Setup Instructions

```
git clone https://github.com/Kunala6051/Fake_AI_Study_Buddy.git
cd Fake_AI_Study_Buddy/Moodio

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open in browser:
👉 http://127.0.0.1:8000/

📌 Project Summary

Moodio blends AI and emotional intelligence to create a personalized learning companion.
It generates study plans, adapts to mood, provides quizzes, and tracks progress in detail.

🔮 Future Enhancements

Mobile app (Android/iOS)

Gamification (XP, badges, streaks)

Advanced emotional analytics

Voice-based assistant

Collaborative group learning
