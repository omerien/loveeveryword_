import tweepy

#Getting token from file
tokenf = open("token")
twitoken = tokenf.read(114)

#Auth tweepy
#Using API v2
client = tweepy.Client(twitoken)
