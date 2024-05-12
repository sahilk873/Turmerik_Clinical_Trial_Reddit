import praw
import openai
import pandas as pd
from typing import List, Dict
from sentiment_analysis import perform_sentiment_analysis_textblob, perform_sentiment_analysis_vader

# Configuration and instance creation
openai.api_key = 'API KEY'
reddit = praw.Reddit(
    client_id='fyBsGjSbqFgv-0BYJDafqA',
    client_secret='2hFFqOXt5aJ4jx5ibVdYE1jp0DpwHA',
    user_agent='turmerikapp by /u/Massive_Decision_191',
)
relevant_subreddits = ['clinicalresearch', 'clinicaltrials', 'clintrials']

def scrape_reddit_data(subreddits: List[str]) -> List[Dict]:
    posts = []
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=100):
            post_data = {
                'title': post.title,
                'text': post.selftext,
                'id': post.id,
                'score': post.score,
                'comments': []
            }
            submission = reddit.submission(id=post_data['id'])
            submission.comments.replace_more(limit=None)

            for comment in submission.comments.list():
                post_data['comments'].append(comment.body)
            posts.append(post_data)
    return posts


def generate_personalized_messages(posts: List[Dict]) -> List[Dict]:
    """
    Generates personalized messages for users based on their interest in clinical trials using OpenAI's GPT model.

    Args:
        posts: A list of dictionaries, each representing a post with title and potentially other data.

    Returns:
        A list of dictionaries where each dictionary has a new key 'message' with a generated personalized message.
    """
    
    for post in posts:
        # Construct the prompt
        prompt = f"Write a professional message to a user about interest in participatingin a clinical trial or just learning more about clinical trials based on this: {post['title'], post['text']}"

        # Call OpenAI's API to generate the completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the message and assign it back to the post dictionary
        post['message'] = response['choices'][0]['message']['content'].strip()
        print(post['message'])

    return posts

def qualified(posts):
    return [post for post in posts if post['sentiment_vader'] > 0.05 and post['sentiment_textblob'] > -0.2]

def assign_sentiment(posts):
    text_blb_sentiment = perform_sentiment_analysis_textblob(posts)
    vader_sentiment = perform_sentiment_analysis_vader(text_blb_sentiment)
    return vader_sentiment
    
def main():
    scraped_data = scrape_reddit_data(relevant_subreddits)
    sentiment_posts = assign_sentiment(scraped_data)
    qualified_posts = qualified(sentiment_posts)
    final_data = generate_personalized_messages(qualified_posts)
    results_df = pd.DataFrame(final_data)
    results_df.to_csv('results.csv', index=False)

if __name__ == '__main__':
    main()

