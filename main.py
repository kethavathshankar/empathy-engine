# main.py
import pyttsx3
from emotion import detect_emotion
from voice import map_emotion_to_voice
import os

def main():
    print("=== The Empathy Engine ===")
    text = input("Enter text to synthesize:\n> ")

    emotion, intensity = detect_emotion(text)

    print(f"\nDetected Emotion: {emotion.upper()}")
    print(f"Emotion Intensity Score: {intensity}")

    engine = pyttsx3.init()

    map_emotion_to_voice(engine, emotion, intensity)

    os.makedirs("output", exist_ok=True)
    output_file = "output/empathy_output.wav"

    engine.save_to_file(text, output_file)
    engine.runAndWait()

    print(f"\nAudio generated successfully: {output_file}")

if __name__ == "__main__":
    main()
