import json
import os

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def load_json_data():
    file_path = os.path.join(os.path.dirname(__file__), "quotes.json")
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error parsing JSON in {file_path}.")
        return None


def generate_wordcloud(data):
    try:
        text = " ".join([quote["quote"] for quote in data])
        wordcloud = WordCloud(width=800, height=400, max_font_size=110).generate(text)
        return wordcloud
    except KeyError:
        print("Invalid data format. Expected 'quote' key in each object.")
        return None


def plot_wordcloud(wordcloud):
    try:
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
    except Exception as e:
        print(f"Error plotting wordcloud: {str(e)}")


def save_wordcloud(wordcloud):
    file_path = os.path.join(os.path.dirname(__file__), "wordcloud.png")
    try:
        wordcloud.to_file(file_path)
    except Exception as e:
        print(f"Error saving wordcloud to {file_path}: {str(e)}")


def main():
    data = load_json_data()
    if data:
        wordcloud = generate_wordcloud(data)
        if wordcloud:
            plot_wordcloud(wordcloud)
            save_wordcloud(wordcloud)


if __name__ == "__main__":
    main()
