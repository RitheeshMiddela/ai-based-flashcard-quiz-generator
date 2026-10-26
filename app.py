import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from google import genai
from pypdf import PdfReader

load_dotenv()  # reads GEMINI_API_KEY from a local .env file (Vercel sets it for us)

# Clean hidden spaces/quotes around the key
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip().strip('"').strip("'")
MODEL = "gemma-4-26b-a4b-it"

# Vercel looks for this top-level "app" variable
app = Flask(__name__, static_folder="public", static_url_path="")


@app.route("/")
def home():
    return app.send_static_file("index.html")


@app.post("/api/generate")
def generate():
    notes = request.form.get("notes", "")

    pdf = request.files.get("pdf")
    if pdf:
        reader = PdfReader(pdf.stream)
        notes = ""
        for page in reader.pages:
            notes += (page.extract_text() or "") + "\n"

    if not notes.strip():
        return jsonify(error="Please paste some notes or upload a PDF first."), 400
    if not API_KEY:
        return jsonify(error="GEMINI_API_KEY is not set. Add it to .env (local) "
                             "or to Environment Variables in Vercel."), 500

    difficulty = request.form.get("difficulty", "Medium")
    if difficulty not in ["Easy", "Medium", "Hard"]:
        difficulty = "Medium"
    # Keep the numbers inside the slider ranges
    num_cards = min(max(int(request.form.get("num_cards", 8)), 3), 20)
    num_questions = min(max(int(request.form.get("num_questions", 5)), 3), 15)

    prompt = f"""From these notes, make {num_cards} flashcards and {num_questions} multiple choice questions.
Make them {difficulty} difficulty.
Reply with ONLY JSON, no extra text, in exactly this format:
{{"flashcards":[{{"q":"...","a":"..."}}],
"quiz":[{{"q":"...","options":["...","...","...","..."],"answer":"exact text of the correct option"}}]}}

Notes:
{notes[:8000]}"""

    text = ""
    try:
        client = genai.Client(api_key=API_KEY)
        r = client.models.generate_content(model=MODEL, contents=prompt)
        text = r.text
        start = text.find("{")
        end = text.rfind("}") + 1
        data = json.loads(text[start:end])
        if "flashcards" not in data or "quiz" not in data:
            raise ValueError("The reply is missing flashcards or quiz.")
        return jsonify(data)
    except Exception as e:
        if "401" in str(e) or "UNAUTHENTICATED" in str(e):
            message = "Google rejected the API key. Create a new key and update GEMINI_API_KEY."
        else:
            message = "Something went wrong. Click Generate again. (" + str(e) + ")"
        # "raw" is the model's reply, shown on the page to help with debugging
        return jsonify(error=message, raw=text), 500


if __name__ == "__main__":
    app.run(debug=True)  # local: python app.py, then open http://localhost:5000
