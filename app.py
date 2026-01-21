from flask import Flask, render_template, request
from emotion import detect_emotion
from voice import generate_voice
import os, time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    emotion = None

    if request.method == "POST":
        text = request.form["text"]

        emotion, intensity = detect_emotion(text)

        os.makedirs("static", exist_ok=True)
        audio_path = "static/empathy_output.mp3"

        generate_voice(text, emotion, audio_path)

        # cache busting
        audio_file = f"{audio_path}?v={int(time.time())}"

    return render_template(
        "index.html",
        audio_file=audio_file,
        emotion=emotion
    )

if __name__ == "__main__":
    app.run(debug=True)
