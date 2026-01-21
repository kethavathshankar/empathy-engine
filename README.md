# The Engine of Empathy
# Emotion-Aware Text to Speech

<p align="center">
  <img src="https://github.com/kethavathshankar/EcoInfinite_Nexu-s/blob/main/ui-preview.png" alt="RecyIndia Logo" width="260"/>
</p>


---

## Overview

The **Empathy Engine** is a Python-driven AI program that can transform texts to audio by modulating voice attributes in response to the detected emotion in the text.

Unlike the usual TTS systems, which produce robot-like and monotoned output, the inclusion of **emotion-aware voice modulation** in the system makes the output more expression-like, thereby sounding human-like.

---

## Problem Statement

On receiving a text input, the system should:

1. Determine the tone of the text from an emotional standpoint.
2. Assign the corresponding voice parameters for the identified emotion

3. Produce an auditable playable voice file that embodies the expression.

---

## Input and Output

# Input
input The text string is provided through a web interface. Example input:

#### Output
- Emotion Identified (Happy / Frustrated / Neutral)
– Audio file for produced speech
- Embedded audio player for listening
---

## Live Deployment Note

This project is built using **Flask (Python backend)** and performs
dynamic emotion detection and audio generation.

⚠️ **GitHub Pages does not support backend frameworks like Flask**,  
so the application cannot be hosted as a live interactive website on GitHub Pages.

### How to Run Locally
```bash
git clone https://github.com/kethavathshankar/empathy-engine
cd empathy-engine
pip install -r requirements.txt
python app.py

Then,Then open Like: http://127.0.0.1:5000
# System Flow

```
class

flowchart TD
A[User Input of Text] → B[Emotion
B -> C{Emotion Type}
C ->|Happy| D[Increase Rate & Volume]
C -->|Frustrated| 
E[Decre
C -->|Neutral| F[Default Voice Settings
D --> G[Text-to-Speech
H --> G
F -> G
G --> H[Generate Audio File]
H --> I[Play Audio in Browser]




