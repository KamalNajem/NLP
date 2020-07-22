# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
pip install twitter_scraper

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

begin_date = dt.date(2020,3,16)
end_date = dt.date(2020,6,20)
limit = 1000 
lang = 'english'

tweets = query_tweets("Coronavirus", begindate = begin_date, enddate = end_date, limit = limit, lang = lang)

df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv('tweet_covid.csv')

import re

def nlp_pipeline(text):

    text = text.lower()
    text = text.replace('\n', ' ').replace('\r', '')
    text = ' '.join(text.split())
    text = re.sub(r"[A-Za-z\.]*[0-9]+[A-Za-z%°\.]*", "", text)
    text = re.sub(r"(\s\-\s|-$)", "", text)
    text = re.sub(r"[,\!\?\%\(\)\/\"]", "", text)
    text = re.sub(r"\&\S*\s", "", text)
    text = re.sub(r"\&", "", text)
    text = re.sub(r"\+", "", text)
    text = re.sub(r"\#", "", text)
    text = re.sub(r"\$", "", text)
    text = re.sub(r"\£", "", text)
    text = re.sub(r"\%", "", text)
    text = re.sub(r"\:", "", text)
    text = re.sub(r"\@", "", text)
    text = re.sub(r"\-", "", text)

    return text

df = pd.read_csv("tweet_covid.csv")

corpus = df['text']
corpus_clean = corpus.apply(nlp_pipeline)


!pip install textblob
!pip install textblob-fr

from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

polarity = []
for text in corpus_clean:
  polarity.append(TextBlob(text,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0])
  
import matplotlib.pyplot as plt

plt.plot(polarity)
  
  
  
  
  
  
  
  
  
  
  
