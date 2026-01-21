# voice.py
def map_emotion_to_voice(engine, emotion, intensity):
    base_rate = 180
    base_volume = 1.0

    if emotion == "happy":
        rate = base_rate + int(40 * abs(intensity))
        volume = min(1.0, base_volume + 0.2)

    elif emotion == "frustrated":
        rate = base_rate - int(30 * abs(intensity))
        volume = base_volume - 0.3

    else:  # neutral
        rate = base_rate
        volume = base_volume

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
