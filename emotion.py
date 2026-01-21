from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.3:
        return "happy", score
    elif score <= -0.3:
        return "frustrated", score
    else:
        return "neutral", score
