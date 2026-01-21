from gtts import gTTS
import os

def generate_voice(text, emotion, output_path):
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)
    return output_path
