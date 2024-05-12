import asyncpraw
import openai
import pandas as pd
import asyncio
from typing import List, Dict
from sentiment_analysis import perform_sentiment_analysis_textblob, perform_sentiment_analysis_vader

# Configuration
openai.api_key = 'sk-proj-SIhTnSKO9NOetMBgGySxT3BlbkFJ3KKoGkEoODeFtO6AEp97'  # Consider securely managing the API key
reddit = asyncpraw.Reddit(
    client_id='fyBsGjSbqFgv-0BYJDafqA',
    client_secret='2hFFqOXt5aJ4jx5ibVdYE1jp0DpwHA',
    user_agent='turmerikapp by /u/Massive_Decision_191',
)
relevant_subreddits = ['clinicaltrials']

async def scrape_reddit_data(subreddits: List[str]) -> List[Dict]:
    posts = []
    for subreddit_name in subreddits:
        subreddit = await reddit.subreddit(subreddit_name)
        async for post in subreddit.hot(limit=100):
            post_data = {
                'title': post.title,
                'text': post.selftext,
                'id': post.id,
                'score': post.score,
                'comments': []
            }
            submission = await reddit.submission(id=post_data['id'])
            submission.comments.replace_more(limit=None)
            posts.append(post_data)
    return posts

async def generate_personalized_messages(posts: List[Dict]) -> List[Dict]:
    for post in posts:
        prompt = f"Write a professional message to a user who is positive about clinical trials based on this title: {post['title']}. Additional Context: Inquire about the interest in joining a clinical trial."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        post['message'] = response['choices'][0]['message']['content'].strip()
    return posts

async def qualified(posts):
    return [post for post in posts if post['sentiment_vader'] > 0.5 and post['sentiment_textblob'] > 0.5]

async def assign_sentiment(posts):
    text_blb_sentiment = perform_sentiment_analysis_textblob(posts)
    vader_sentiment = perform_sentiment_analysis_vader(text_blb_sentiment)
    return vader_sentiment

async def main():
    scraped_data = await scrape_reddit_data(relevant_subreddits)
    posts_sentiment = await assign_sentiment(scraped_data)
    qualified_posts = await qualified(posts_sentiment)
    print(len(qualified_posts))
    final_data = await generate_personalized_messages(qualified_posts)
    results_df = pd.DataFrame(final_data)
    results_df.to_csv('results.csv', index=False)

asyncio.run(main())
