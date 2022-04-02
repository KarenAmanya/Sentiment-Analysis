import requests
import tweepy
import rfc3339 as RF
import datetime
import pandas as pd
import json

consumer_key='qplZal1EsUJMnzP1XKGOBWq5D'
consumer_secret_key='vFTDMpAKaytsv1RNTZrNQtVHaiwE1CQjQXL5g3cgAhYrhRpkXZ'
Bearer_token='AAAAAAAAAAAAAAAAAAAAAJcCaQEAAAAAPte8oxsY5KoBNZQ5XPR7y%2BRPrd0%3DpvGUPzr3tvB36EZwnlNh33e2E4csVvIthC9lx17dxGVjWyRkH2'
access_token='918508291063500800-DofaNMZVlgdSmnvTOTI2igBPNi049XZ'
access_token_secret='ErzZCL3CQoHxzDlDqqz1yZuv4hCuuSPY1xCcJ75c9kn2W'

callback_uri='oob'
#To create the authentication object
auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key,callback_uri)
acc_url='https://api.twitter.com/2/tweets/search/recent?'
hashtag_url='https://api.twitter.com/1.1/search/tweets.json?'
#To set the access token and secret
auth.set_access_token(access_token,access_token_secret)
#To create the API object
api=tweepy.API(auth,wait_on_rate_limit=True)

#To create a header
def create_header(bearer_token):
    headers={'Authorization': f"Bearer {bearer_token}"}
    return headers

#To create parameters
def create_parameters(handle,From,To,Items):
    parameters={'query':handle,
                'start_time':RF.format(pd.to_datetime(From)),
                'end_time':RF.format(pd.to_datetime(To)),
                'max_results':Items,
                }
    return parameters


#To request data from an account and  store the result in a json file
def fetch_account_tweets(Parameters,Headers):
    with open('DATA.json',mode='w') as data_file:
        response_1=requests.get(acc_url,params=Parameters,headers=Headers).json()
        json.dump(response_1,data_file)

#To request data from a hashtag and store the result in a json file
def fetch_hashtag(Parameters,Headers):
    with open('DATA.json',mode='w') as data_file:
        response_2=requests.get(hashtag_url,params=Parameters,headers=Headers).json()
        json.dump(response_2,data_file)


Headers=create_header(Bearer_token)
Parameters=create_parameters(handle='Coopbankenya',From='2022-03-26',To='2022-03-27',Items=100)
fetch_account_tweets(Parameters=Parameters,Headers=Headers)