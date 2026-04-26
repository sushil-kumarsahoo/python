def get_sentiment(text):
    positive_words = ["love", "good", "fantastic", "great"]
    negative_words = ["bad", "terrible", "worst"]

    text = text.lower()

    if any(word in text for word in positive_words):
        return "positive"
    elif any(word in text for word in negative_words):
        return "negative"
    else:
        return "neutral"

# Test
texts = ["I love this", "This is not bad", "It is okay"]

for t in texts:
    print(t, "->", get_sentiment(t))