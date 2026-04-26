import pandas as pd

# Sample dataset
data = {
    "text": ["I don't love this product", "This is bad", "Amazing experience"],
    "label": ["negetive", "negative", "positive"]
}

df = pd.DataFrame(data)
print(df)