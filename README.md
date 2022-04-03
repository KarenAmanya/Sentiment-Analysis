# Twitter-Sentiment-Analysis
A sentiment analysis of a Kenyan bank using tweets. The tweets were sourced using the Twitter API and tweepy, a python library for accessing the twitter API.

### Objective 1:To find out the overall sentiment of the bank's customer's based on their tweets.

1. Irrelevant tweets accounted for the larger percentage, these are tweets meant for advertisemnt purposes and were not specifically directed at the bank.
2. Negative tweets were the second larget group
3. Requests and inquiries came third, these are tweets requesting the bank admin to respond or questions regarding the banks services.
4. Positive tweets came last with suggestions which I had to exclude from the analysisas the model would not take in a category with only one observation.

![Overall_categories](https://user-images.githubusercontent.com/90700143/161418549-6203c118-e4a7-49c3-aad4-72b94eed94bb.png)


### Objective 2: To compare Positive and Negative tweets
The comparison was quite large , with positive tweets not amounting to even half of the negative tweets


![Pos_vs_neg](https://user-images.githubusercontent.com/90700143/161418594-c3a11f81-c995-4759-b42e-b4dd4318a4c0.png)


### Objective 3: To train the sentiment analysis model to classify tweets as either irrelevant, negative, positive or inquiry/request
Used Sklearn's train_test_split to train the models

#### Model 1: Using Multinomioal naive bayes to predict tweet labels: Achieved an accuracy of 67.8%

![Multinomial_NB](https://user-images.githubusercontent.com/90700143/161418857-9eb599d7-12be-44f3-906b-49880a7d5996.png)


#### Model 2: Using SVM(Support vector machines): Achieved an accuracy of 66.7%, a little lower than Multinomial NB

![SVM](https://user-images.githubusercontent.com/90700143/161418976-8b520e44-0064-4128-8b90-6ebdebee420c.png)

### Objective 4: To find the most mentioned aspects throughout the tweets'
Used RegEx to search for the bank's popular services such as the mobile banking app, online banking , customer service e.t.c

![Aspects](https://user-images.githubusercontent.com/90700143/161419186-eb7b978e-64b7-4fae-8185-7570627bc4be.png)

