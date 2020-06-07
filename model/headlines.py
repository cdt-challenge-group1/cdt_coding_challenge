from newsapi import NewsApiClient
import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import datetime, timedelta


def add_headlines(new_headlines, date, current_headlines):
    for article in new_headlines['articles']:
        if article['description'] is None:
            description = ''
        else:
            description = article['description']
        headline = article['title'] + '. ' + description
        current_headlines.append({'content': headline, 'date': date})
    return current_headlines


def save_headlines(headlines_today):
    '''
    Implement saving new headlines
    '''
    return


def collect_and_analyse_headlines():

    newsapi = NewsApiClient(api_key='d334f8b261e9472585644da5b59127fa')

    headlines_today = []

    topics_to_search = ['oil', 'stock']

    # Yesterday's headlines will be grabbed
    date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

    for topic in topics_to_search:
        headlines = newsapi.get_everything(qintitle=topic,
                                           language='en',
                                           from_param=date, to=date)
        headlines_today = add_headlines(headlines, date, headlines_today)

    sid = SentimentIntensityAnalyzer()
    for i, headline in enumerate(headlines_today):
        ss = sid.polarity_scores(headline['content'])
        headlines_today[i]['score'] = ss['compound']

    save_headlines(headlines_today)

    return headlines_today
