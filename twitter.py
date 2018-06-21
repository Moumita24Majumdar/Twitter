import tweepy

from textblob import TextBlob

Consumer_Key = "7yIuzHUQncsoWuWiLV3uAty1K"
Consumer_Secret_Key = "RH1DnMND5zfE5F0eq3JFgg3zIRwiKizvLn9Y4vYkol3q0EKzd8"
Access_Token = "976677595633733633-mJHb0QhZsotwGJtFtt1tIltF5gOkFrx"
Access_Token_Secret = "VZsDEcswKjE09Z5lqnTCeaotde8QoXV3sKgERVtD9pXZJ"

#OAuthHandler

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret_Key)#key
auth.set_access_token(Access_Token,Access_Token_Secret)#access
api = tweepy.API(auth)#login

public_tweets = api.search("Narendra Modi")
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print("")