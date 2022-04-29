
from cleaner import *

Tweets=pd.read_csv('Data\coop2.csv').drop('user_id',axis=1)
cleaned_tweets=clean_data(Tweets)

#A df to keep count of the number of tweets about each aspect
all_aspects=pd.DataFrame(columns=['App','Mcoop','Customer_service','Internet_banking'])

#to find positive matches of 'app'
def app_mentions(tweet):
    match=re.search(r'\b app \b',tweet,re.IGNORECASE) or  re.search(r'\b App \b',tweet)  or re.search(r'\b APP \b',tweet)
    if match:
        return True
    else:
        return False

#to find positive matches of 'mcoop' and 'ussd' 
def mcoop_mentions(tweet):
    #to find positive matches of 'app'
    match=re.search(r'\b mcoop \b',tweet,re.IGNORECASE) or re.search(r'\b USSD \b',tweet) or re.search(r'\b Mcoop \b',tweet)
    if match:
        return True
    else:
        return False

#to find positive matches of 'service'
def service_mentions(tweet):
    #to find positive matches of 'app'
    match=re.search(r'\b service \b',tweet,re.IGNORECASE) or re.search(r'\b services \b',tweet)
    if match:
        return True
    else:
        return False

#to find positive matches of 'Internet banking'
def InternetBanking_mentions(tweet):
    #to find positive matches of 'app'
    match=re.search(r'\b internet \b',tweet,re.IGNORECASE) or re.search(r'\b internet banking \b',tweet) or re.search(r'\b online banking \b',tweet)
    if match:
        return True
    else:
        return False
    

App=[]
Mcoop=[]
Customer_service=[]
Internet_banking=[]

All_tweets=[tweet for tweet in cleaned_tweets.text]

for tweet in All_tweets:
    if app_mentions(tweet) ==True:
        tweet=tweet+','
        App.append(tweet)
        
    if mcoop_mentions(tweet)==True:
        tweet=tweet+','
        Mcoop.append(tweet)
    
    if service_mentions(tweet)==True:
        tweet=tweet+','
        Customer_service.append(tweet)
        
    if InternetBanking_mentions(tweet)==True:
        tweet=tweet+','
        Internet_banking.append(tweet)


#To add all positive matches of all aspects to the DF
all_aspects['App']=pd.Series(App)
all_aspects['Mcoop']=pd.Series(Mcoop)
all_aspects['Customer_service']=pd.Series(Customer_service)
all_aspects['Internet_banking']=pd.Series(Internet_banking)

for col in all_aspects.columns:
    cols=all_aspects.columns

values=[all_aspects['App'].count(),all_aspects['Mcoop'].count() ,all_aspects['Customer_service'].count() ,all_aspects['Internet_banking'].count()]
aspect_count=pd.DataFrame(columns=['Aspect','Count'])
aspect_count.Aspect=cols
aspect_count.Count=values
aspect_count.sort_values(by='Count',ascending=True,inplace=True)

counts=[]
Aspects=[]
for num in aspect_count.Count:
    counts.append(num)
for asp in aspect_count.Aspect:
    Aspects.append(asp)

print(Aspects)