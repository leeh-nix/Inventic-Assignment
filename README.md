# 💬 Nikheel's Inventic Assignment 

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nikheel-inventic.streamlit.app/)

## Assignment

### Task:
Write a Python script that analyzes a given book passage (provided below) and provides the following information:
1. The total number of words in the passage.
2. The predominant emotion conveyed in the passage (e.g., joy, sadness, anger).
3. 2-3 possible books the passage might be from.
4. A summary of the passage in 2-3 sentences.

### Instructions:
- The passage will be given as input by me, so your script should be able to take it as a text input (e.g., a hardcoded string or input from a file).
- Your script should be modular and well-commented, making it easy to understand and maintain.

## Solution:

- The app uses Gemini AI to generate the summary and find the book's author to which the passage belongs.
- The app also uses NLTK to analyze the word count and sentiment of the passage or the book.
- The front end is made with Streamlit and is deployed in its cloud.

### How to run it on your machine

1. Install the requirements

```sh
$ pip install -r requirements.txt

```

2. Run the app

```sh
$ streamlit run streamlit_app.py

```
