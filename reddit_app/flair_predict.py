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

def clean_text(text):
    '''
    function to preprocess and clean the data before passing the data to model

    parameters :
        args :
        text (str) : raw unprocessed text

    returns :
        text (str) : preprocessed text ready to be passed onto the model pipeline
    '''
    STOPWORDS = set(stopwords.words('english'))
    text = text.lower()
    text = re.compile('[/(){}\[\]\|@,;]').sub(' ', text)
    text = re.compile('[^0-9a-z #+_]').sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS and word not in punctuation)
    return text

def detect_flair(input_url, api=False):
    '''
    main function for getting the predictions back to the flask app

    parameters :
        args :
        input_url (str) : url input by the user on the home page
        api (bool) : boolean value indicating if it an testing endpoint or normal endpoint.
            Depending on this value, results have to be modified before getting back to the flask app.
    '''

    result = []

    headers = {'User-Agent': 'Mozilla/5.0'}
    CLIENT_ID = "#########"
    CLIENT_SECRET = "************"
    REDIRECT_URI = "http://localhost:8080"
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=headers)
    try:
        submission = reddit.submission(url=input_url)
        title = clean_text(submission.title)
        model = joblib.load('model.pkl')
    except Exception as error:
        return

    if not api:
        result.append(('Title ', submission.title))
        result.append(('URL ', input_url))
        result.append(('Created Time(UTC) ', datetime.datetime.fromtimestamp(int(submission.created_utc)).strftime('%Y-%m-%d %H:%M:%S')))
        result.append(('Flair detected ', model.predict([title])))

    else:
        result.append(model.predict([title]))

    return result
