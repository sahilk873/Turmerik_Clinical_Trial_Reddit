import json
import re
from llamaapi import LlamaAPI
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

llama = LlamaAPI("LL-tgPtDwuIROTSjbgSdqTk7vC0WT5VQZAjpaw1XSpNvpsZLdht1ANQeO7yLrV6MwCR")

def perform_sentiment_analysis_llm(posts):
    """
    Performs sentiment analysis on post titles, text, and comments.
    Enhances focus on identifying interest in clinical trial participation by expanding keyword search.

    Args:
        posts: List of dictionaries containing post data and comments.

    Returns:
        A list of dictionaries with sentiment scores and clinical trial interest scores added, based on an expanded set of keywords.
    """
    for post in posts:
        text = ' '.join([post['title'], post['text']] + post.get('comments', []))
        api_request_json = {
            "messages": [
                {
                    "role": "user",
                    "content": f"On a scale from -1 to 1, assess the sentiment of the text as it relates to general attitude and interest levels regarding clinical trials. Only return the number itself, no other text. A score of -1 would indicate strong opposition to clinical trials, 0 would indicate neutrality, and a score of 1 would indicate strong support and positive sentiment towards clinical trials. This is the text: {text}", 
                }
            ],
            "max_length": 500,
            "temperature": 0.1,
            "top_p": 1.0,
            "frequency_penalty": 1.0
        }
        response = llama.run(api_request_json)
        response_json = json.dumps(response.json(), indent=2)
        pattern = r'"content":\s*"([\-+]?[0-9]*\.?[0-9]+)"'
        match = re.search(pattern, response_json)
        number = float(match.group(1))
        post['sentiment_llm'] = number

    return posts

def perform_sentiment_analysis_textblob(posts):
    """
    Performs sentiment analysis using TextBlob on post titles, text, and comments.
    
    Args:
        posts: List of dictionaries containing post data and comments.

    Returns:
        A list of dictionaries updated with sentiment scores.
    """
    for post in posts:
        text = ' '.join([post['title'], post['text']] + post.get('comments', []))
        analysis = TextBlob(text)
        post['sentiment_textblob'] = analysis.sentiment.polarity  # -1 to 1 scale, where 1 is very positive

    return posts

nltk.download('vader_lexicon')

def perform_sentiment_analysis_vader(posts):
    """
    Performs sentiment analysis using VADER on post titles, text, and comments.
    
    Args:
        posts: List of dictionaries containing post data and comments.

    Returns:
        A list of dictionaries updated with sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    for post in posts:
        text = ' '.join([post['title'], post['text']] + post.get('comments', []))
        score = sia.polarity_scores(text)
        post['sentiment_vader'] = score['compound']  # Compound score

    return posts




