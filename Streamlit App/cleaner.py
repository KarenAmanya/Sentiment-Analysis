import re
import pandas as pd
import numpy as np


tweets=pd.read_csv('Data\coop2.csv').drop('user_id',axis=1)

clean_tweets=[]
def clean_data(Data):
    for tweet in Data.text:
        tweet=re.sub("@[A-Za-z0-9]+", repl=' ',string=tweet)#removes @username/mentions
        tweet=re.sub('[^a-zA-Z]', repl=' ',string=tweet)#removes punctuations + special chars
        tweet=re.sub('(?:(https|http)\s?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)* ',repl=' ',string=tweet)#removes links
        clean_tweets.append(tweet)
    Data['text']=pd.Series(clean_tweets)
    return Data

tweets=clean_data(tweets)
sentiment=pd.DataFrame(tweets.groupby('label',as_index=False).agg({'text':pd.Series.count}))
#sentiment=sentiment.astype('str')
values=[i for i in sentiment.text]
print(values)


