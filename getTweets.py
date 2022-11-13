# import the tweepy library
import tweepy
# import the config file
import config
# create client with tweepy.Client with consumer key and consumer secret and access token as arguments
client = tweepy.Client(consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET_KEY,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)

# get my most liked tweet
client.get_tweet( )
