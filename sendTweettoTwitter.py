# importar librerias necesarias para el funcionamiento del script
import tweepy
# import config
import config

# create client with tweepy.Client with consumer key and consumer secret and access token as arguments
client = tweepy.Client(consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET_KEY,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)
# create a variable called tweet with string that says 'I wrote this tweet with Copilot and I'm at the Women in Tech Boston conference'
tweet = 'I wrote this tweet with Copilot and I\'m at the Women in Tech Boston conference'

# send a tweet with client.create_tweet() method and tweet as argument
client.create_tweet(text=tweet)

# print a message that says 'Tweet sent'
print('Tweet sent')
