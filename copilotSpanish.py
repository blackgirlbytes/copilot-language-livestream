# enviar tweet

# importar archivo de configuracion
import config

import tweepy
# create client with tweepy.Client with consumer key and consumer secret and access token as arguments

# crear cliente con tweepy.Client con consumer key y consumer secret y access token como argumentos

client = tweepy.Client(consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET_KEY,
                       access_token=config.ACCESS_TOKEN,
                       access_token_secret=config.ACCESS_TOKEN_SECRET)


# autenticación
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# variable con el texto del tweet
tweet = "Hola, soy un tweet enviado desde Python"

# enviar tweet con el texto de la variable tweet
response = client.create_tweet(text=tweet)



# imprimir respuesta
print(response)