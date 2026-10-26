<div align="center">

# 📚 AI Study Flashcard & Quiz Generator

### Paste your notes or upload a PDF. Get flashcards and a quiz in seconds.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Built%20with-Flask-000000?logo=flask&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-000000?logo=vercel&logoColor=white)
![Gemma 4](https://img.shields.io/badge/AI-Gemma%204-4285F4?logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-6366F1)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-22D3EE)

</div>

---

## ✨ What it does

Studying from long notes is slow. This app turns your notes into **active-recall practice** automatically: flashcards to review, and a multiple-choice quiz to test yourself.

| | Feature | Details |
|---|---|---|
| 🃏 | **Flashcards** | Question-and-answer cards. Click a card to reveal the answer. |
| 📝 | **Quiz** | Multiple-choice questions with a score on submit (balloons for a perfect score 🎈). |
| 📄 | **PDF upload** | Upload a PDF instead of pasting text (up to 4 MB). |
| 🎚️ | **Difficulty** | Easy, Medium or Hard. |
| 🔢 | **You choose the size** | 3 to 20 flashcards and 3 to 15 quiz questions. |
| ⬇️ | **Download** | Save your flashcards as `flashcards.txt`. |
| 🌌 | **Modern dark UI** | Glassmorphism cards, glow background, fully responsive. |

---

## 🧭 How it works

```
 Notes / PDF  ──►  Gemma 4 (Google AI)  ──►  Flashcards + Quiz  ──►  Study & score
```

1. Paste notes or upload a PDF.
2. Pick the difficulty and how many cards and questions you want.
3. Click **Generate**.
4. Flip through the flashcards, then take the quiz and see your score.

---

## 🚀 Run it yourself

**1. Install the dependencies**

```bash
pip install -r requirements.txt
```

**2. Add your API key**

Create a file named `.env` in the project folder:

```
GEMINI_API_KEY=your-key
```

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey). Keep this file private. It is listed in `.gitignore`, so git never uploads it.

**3. Start the app**

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

> 💡 **Tip:** On Windows, use `py -m pip install -r requirements.txt` and `py app.py`.

---

## ☁️ Deploy on Vercel

1. Import the GitHub repo into [Vercel](https://vercel.com/new). It detects the Flask app in `app.py` automatically.
2. In **Settings → Environment Variables**, add `GEMINI_API_KEY` with your key.
3. Deploy (or redeploy if you added the key after the first deploy).

---

## 🗂️ Project structure

```
study-app/
├── app.py             # the server: PDF reading, AI call (POST /api/generate)
├── public/
│   └── index.html     # the page: layout, dark theme, flashcards, quiz, download
├── requirements.txt   # Python packages
└── README.md
```

---

## 🛠️ Built with

- [Flask](https://flask.palletsprojects.com): the Python server
- [Vercel](https://vercel.com): hosting
- [Gemma 4](https://ai.google.dev/gemma) via the Google GenAI SDK: generates the flashcards and quiz
- [pypdf](https://pypi.org/project/pypdf/): reads text from uploaded PDFs

---

## 🏆 Made for

**MLH Hacktoberfest Hack Day Amaravati** x AI-Based Productivity Tools Club, VIT-AP.

## 📄 License

Released under the [MIT License](LICENSE). Free to use, change and share.

<div align="center">

Made with ❤️ by students, for students.

</div>
