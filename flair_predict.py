import joblib
import os
from bs4 import BeautifulSoup
import re
from string import punctuation
import time
import datetime
import praw
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
import sklearn
from praw.models import MoreComments


def clean_text(text):
    STOPWORDS = set(stopwords.words('english'))
    text = text.lower()
    text = re.compile('[/(){}\[\]\|@,;]').sub(' ', text)
    text = re.compile('[^0-9a-z #+_]').sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS and word not in punctuation)
    return text

def detect_flair(input_url, api=False):

    result = []

    headers = {'User-Agent': 'Mozilla/5.0'}
    CLIENT_ID = "KQM6inEn8fZ-Fw"
    CLIENT_SECRET = "6J8QSu7mP8L2Un9LHZi2svulFxs"
    REDIRECT_URI = "http://localhost:8080"
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=headers)
    try:
        submission = reddit.submission(url=input_url)
        comment = " "
        count_comment = 0
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            comment = comment + " " + top_level_comment.body
            count_comment += 1
            if count_comment > 10:
                break
        title = submission.title
        text = clean_text(submission.title + comment)
        model = joblib.load('model_sgd.pkl')
    except Exception as error:
        return

    if not api:
        result.append(('Title ', submission.title))
        result.append(('URL ', input_url))
        result.append(('Created Time(UTC) ', datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')))
        result.append(('Flair detected ', model.predict([text])))

    else:
        result.append(model.predict([title]))

    return result
