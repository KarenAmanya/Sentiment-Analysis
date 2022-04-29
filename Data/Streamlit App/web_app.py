from gettext import npgettext
import streamlit as st
import os
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from cleaner import *
from aspects import *
import matplotlib.pyplot as plt
import plotly.graph_objects as plotly
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score




# Header
header=st.container()
dataset=st.container()
chart=st.container()
features=st.container()
modelTraining=st.container()
user_inputs=st.container()

with header:
    st.title('A Twitter Sentiment Analysis of Coop Bank Kenya')
    st.text("In this project I look into the sentiment of the bank's customers based on their tweets")

with dataset:
    st.subheader('A dataset of tweets directed at the bank')
    st.text("I used the twitter API and tweepy to fetch tweets within a one month timespan.")
    all_tweets=pd.read_csv('Data\coop2.csv').drop('user_id',axis=1)
    #st.write(all_tweets.head())
    st.text('I then performed some cleaning of the tweets and categorized them as;')
    st.text('1. Negative - tweets protraying negative opinions/ comments')
    st.text('2. Positive - tweets protraying positive opinions/ comments')
    st.text('3. Irrelevant - irrelevant tweets i.e marketing,retweets etc')
    st.text('4. Requests - tweets requesting the admin to respond / making inquiries.')
    st.text('4. Inquiry - tweets making inquiries.')
    cleaned_tweets=clean_data(all_tweets)
    st.write(cleaned_tweets.head())
    st.subheader("Overall Sentiment of Coop-Bank Customer's")
    sentiment=tweets.groupby('label',as_index=False).agg({'text':pd.Series.count})
    labels=[]
    values =[]
    for i in sentiment.label:
        labels.append(i)
    for j in sentiment.text:
        values.append(j)

with chart:
    #The plot
    st.subheader('Categories of Tweets')
    fig = plotly.Figure(
          plotly.Pie(
         labels =labels,
         values = values,
         hole=0.5,
         hoverinfo = "label+percent",
         textinfo = "value"
     ))
    st.plotly_chart(fig)

    pos_vs_neg=pd.DataFrame({'Sentiment':['Negative','Positive'],'Count':[173,11]})
    st.subheader('Positive vs. Negative Tweets')
    fig = plotly.Figure(
          plotly.Pie(
         labels =pos_vs_neg.Sentiment,
         values = pos_vs_neg.Count,
         hoverinfo = "label+percent",
         textinfo = "value"
     ))
    st.plotly_chart(fig)



with features:
    #To display the various aspects found from the tweets
    st.subheader('A Visual Representation of How Often the Main Aspects of Coop Bank are mentioned in Tweets')
    fig =plotly.Figure(
            plotly.Bar(
                y=aspect_count['Aspect'],
                x=aspect_count['Count'],
                orientation='h'
        ))
    st.plotly_chart(fig)
    st.text('The data shows that the most talked about aspect of the bank is their mobile app , followed by the customer service.')

with modelTraining:
    st.header('Training of a model to classify tweets according to the 4 categories.')
    #Vectorizing adn tokenizing X
    Countvectorizer=CountVectorizer()
    tweets=all_tweets.text
    X=Countvectorizer.fit_transform(tweets).toarray()
    y=all_tweets.label.values

    #Split data in the ration 70:30
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.3,stratify=y)

    #Fit the model
    multinomialNB=MultinomialNB()
    multinomialNB.fit(X_train,y_train)

    #to predict values
    y_pred=multinomialNB.predict(X_test)
    
    #Results
    accuracy=round(accuracy_score(y_test,y_pred)*100)
    classification_score=classification_report(y_test,y_pred,target_names=['Inquiry','Irrelevant','Negative','Positive','Request'],labels=[0,1,2.3,4],output_dict=True)
    y_pred_array=Countvectorizer.fit_transform(y_pred).toarray()
    y_test_array=Countvectorizer.fit_transform(y_test).toarray()

    #To compare the actual vs predicted values
    comparison=pd.DataFrame({'Actual_values':y_test,'Predicted_values':y_pred})

    #To display the model results
    #display_col=st.columns(2)
    st.subheader('Tweet label classification using MultiNomial Naive Bayes')
    st.write(comparison.tail())
    st.write('How the model performed:')
    st.text(f'The model scored an accuracy of {accuracy}%, A fair performance considering the tweets are in mixed languages of English , Swahili and Sheng')
    
    #Tweet classifixcation with SVM
    linearsvc=LinearSVC()
    linearsvc.fit(X_train,y_train)

    #predicting the labels
    y_pred2=linearsvc.predict(X_test)

    #To compare the actual vs predicted values
    comparison_2=pd.DataFrame({'Actual_values':y_test,'Predicted_values':y_pred2})
    #Results
    svm_accuracy=round(accuracy_score(y_test,y_pred2)*100)
    st.subheader('Tweet label classification using SVM')
    st.write(comparison_2.head())
    st.write('How the model performed:')
    st.text(f'The model scored an accuracy of {svm_accuracy}%, Slightly better than Multinomial NB')
    

