import tweepy

#auth tweepy
auth = tweepy.OAuth2BearerHandler("TOKEN (not public lmao)")
api = tweepy.API(auth)
