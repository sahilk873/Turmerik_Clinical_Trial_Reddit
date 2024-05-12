# Turmerik_Clinical_Trial_Reddit

Setup Instructions
Prerequisites: Ensure you have Python 3.8 or higher installed on your machine.
Dependencies: Install the required Python libraries using:
bash
Copy code
pip install -r requirements.txt
Running the Code:
To run the synchronous script, use:
bash
Copy code
python main.py
For the asynchronous script, use:
bash
Copy code
python async_main.py
Methodology
This project uses the Reddit API to collect posts and comments, which are then analyzed using sentiment analysis techniques to determine the emotional tone. The main.py script performs synchronous processing, while async_main.py uses asynchronous calls for efficiency.

Challenges
Managing API rate limits with praw and asyncpraw.
Ensuring accurate sentiment detection across diverse text data.
Examples
Data Collected: Posts and comments from specified subreddits.
Analysis Performed: Sentiment analysis using TextBlob and custom functions in sentiment_analysis.py.
Messages Generated: Logs and outputs categorizing sentiments as positive, negative, or neutral.
Ethical Considerations
Data Privacy: No personal data is stored or processed.
Bias Mitigation: Techniques were employed to reduce bias in sentiment assessment.
Transparency: All methods and algorithms are fully disclosed in the script comments.
