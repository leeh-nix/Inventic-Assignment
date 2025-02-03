from nltk import download
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

from utils.gemini import geminiai

download("punkt")  # tokenizer model
download("vader_lexicon")  # Valence Aware Dictionary and sEntiment Reasoner


# Function for word count
def word_count(passage):
    words = word_tokenize(passage, preserve_line=False)
    words = [word for word in words if word.isalpha()]
    return len(words)


# analyze the passage and return the predominant emotion
# Note: SentimentIntensityAnalyzer ignores text written in #hashtag
def emotion_analysis(passage):
    """
    Analyzes the given passage to determine the predominant emotion.

    This function utilises the SentimentIntensityAnalyzer from NLTK to 
    assess the sentiment of the passage and categorizes it into one of 
    three emotions: "Joy", "Sadness", or "Neutral", based on the 
    compound sentiment score.

    Args:
        passage (str): The passage of text to analyze.

    Returns:
        str: The predominant emotion in the passage, which can be 
        "Joy", "Sadness", or "Neutral".
    """    
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(passage)
    compound_score = sentiment_scores["compound"]

    if compound_score >= 0.05:
        return "Joy"
    elif compound_score <= -0.05:
        return "Sadness"
    else:
        return "Neutral"


# Main function to analyze the passage
def generate_response(passage):
    word_count_result = word_count(passage)
    emotion = emotion_analysis(passage)
    summary = geminiai(passage)

    return f"Word Count: {word_count_result} \n\n Emotion: {emotion} \n\n {summary}"
