# emotion.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        emotion = "happy"
    elif compound <= -0.05:
        emotion = "frustrated"
    else:
        emotion = "neutral"

    return emotion, compound
