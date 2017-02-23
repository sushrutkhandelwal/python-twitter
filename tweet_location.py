import tweepy

consumer_key = 'YOUR_CONSUMER_KEY' 
consumer_secret = 'YOUR_CONSUMERKEY_SECRET' 
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#"where on earth id" of india = 23424848
#link to get "where on earth id" of your desired location
#http://woeid.rosselliot.co.nz/
trendsInd = api.trends_place(23424848) 

data = trendsInd[0] 
trends = data['trends']
names = [trend['name'] for trend in trends]

print "Most trending in India: "+names[0]+'\n'
print "Other Trends: "
for trend in names:
    print trend