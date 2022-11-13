# import the tweepy library
import tweepy
# import config file
import config

# create client object with tweepy.Client
client = tweepy.Client(consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET_KEY,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

# create a variable called tweet with string that says 'I wrote this tweet with Copilot and I'm at All Things Open'
TWEET = 'I wrote this tweet with Copilot and I\'m at All Things Open'

# send a tweet with client.create_tweet() method and tweet as argument
response = client.create_tweet(text=TWEET)
# print response
print(response)
print('Tweet sent')
