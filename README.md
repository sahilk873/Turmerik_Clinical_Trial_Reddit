# Reddit Sentiment Analysis Tool

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Required Python libraries (see Installation)

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Installation of Dependancies
Install the required Python libraries using:

```bash
pip install -r requirements.txt
```

#### Running the Code
To run the synchronous script, use:

```bash
python main.py
```

For the asynchronous script, use:
```bash
python async_main.py
```

## Configuration
- Obtain Reddit API (PRAW) Key
- Obtain OpenAI API Key
- Choose specific subreddits of choices (e.g. clinicaltrials, clinicalresearch, clintrials)

## Methodology
This project uses the Reddit API to collect posts and comments, which are then analyzed using sentiment analysis techniques to determine the tone towards clinical trials, health, and medicine in general. The main.py script performs synchronous processing, while async_main.py uses asynchronous calls for efficiency.

## Challenges
- Managing API rate limits with praw, asyncpraw, and openai.
- Managing asynchronous functional calls with asynchio.
- Ensuring accurate sentiment detection across diverse text data.

## Examples
### Data Collected
 - A post's title, text, and comments are analyzed using sentiment analysis. After, promising posts are responded to using an OpenAI prompt.
### Example message generated:

Dear [User],

I hope this message finds you well. I wanted to reach out to share information about an opportunity to support clinical research education and accessibility this holiday season. We noticed you have a particular affinity for giving during the holiday season and would love to expand this to the realm of clinical trials. We are dedicated to advancing clinical trials and research for the benefit of patients and healthcare advancement.     

If you're interested in learning more about participating in a clinical trial or gaining more information about clinical research, we would love to provide you with resources and guidance. Your interest and support can help contribute to groundbreaking research and advancements in healthcare.

Please feel free to reach out to us if you have any questions or if you would like to explore this opportunity further. Your participation and engagement in clinical research can make a meaningful impact on the future of healthcare.

Thank you for considering supporting clinical research education and accessibility.

Warm regards,

[Your Name]
[Title/Role]
[Contact Information]


## Analysis Performed
-Sentiment analysis using TextBlob and Vader in sentiment_analysis.py.
- Logs and outputs categorizing sentiments as positive, negative, or neutral.

## Ethical Considerations
- Data Privacy: No personal data is stored or processed.
- Bias Mitigation: Techniques were employed to reduce bias in sentiment assessment.
- Transparency: All methods and algorithms are fully disclosed in the script comments.
