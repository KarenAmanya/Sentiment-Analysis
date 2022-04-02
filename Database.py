from calendar import c
import psycopg2
import json


try:
    conn=psycopg2.connect(dbname='Test',user='postgres', password='2006',port=5432)#establish connection with db
    cursor=conn.cursor()

    create_script=""" CREATE TABLE IF NOT EXISTS coopbanktweets (
                                                            user_id  VARCHAR(500) ,
                                                            text VARCHAR (500)
                                                            )"""
    cursor.execute(create_script)

    insert_script=""" INSERT INTO coopbanktweets (user_id,text) VALUES (%s,%s)"""
    #Load tweets from json file 
    Data_file=open('DATA.json')
    All_tweets=json.load(Data_file)
    for tweet in All_tweets['data']:
        id=int(tweet['id'])
        text=tweet['text']
        #To insert the values to the table
        insert_values=[(id,text)]
        for value in insert_values:
            cursor.execute(insert_script,value)

    conn.commit()

except Exception as error:
    print(error)

#finally:
    #cursor.close()
    #conn.close()





    