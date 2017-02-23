from twython import Twython
from textblob import TextBlob
import re

#sentiment analysis using text blob
def get_sentiment(tweet):
        result = TextBlob(tweet)
        if result.sentiment.polarity > 0:
            return 'positive'
        elif result.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def str_clean(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

consumer_key = 'YOUR_CONSUMER_KEY' 
consumer_secret = 'YOUR_CONSUMERKEY_SECRET' 
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_TOKEN_SECRET'

twit = Twython(app_key=consumer_key, app_secret=consumer_secret, oauth_token=access_token, oauth_token_secret=access_token_secret)

#your keyword to find related tweets
query='#Budget2017'
n=100

#this case is for mixed tweets, that is recent and popular
#result_type can be popular also. lang=en --> This case is for english tweets only.
search = twit.search(q=query, count=n, lang='en', result_type='mixed')

tweets = search['statuses']
cleanTweets=[]

positive_score=0

for tweet in tweets:
	cleanTweets.append(str_clean(tweet['text']))

for i in range(len(cleanTweets)):
	print cleanTweets[i]+'\n'
	sent=get_sentiment(cleanTweets[i])
	if sent=="positive":
		positive_score+=1
	elif sent=="negative":
		positive_score-=1

#positivity score defined here is the difference of positive tweets and negative tweets divided by total number of tweets
print "\n\n\nPositivity score from -1 to 1: "+str(float(positive_score)/float(n))