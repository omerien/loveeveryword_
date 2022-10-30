import tweepy

#Getting keys from file
tokenf = open("token")
bearertoken = tokenf.read(114)


#Auth tweepy
#Using API v2
client = tweepy.Client(bearer_token=bearertoken, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None, *, return_type=Response, wait_on_rate_limit=False)


#Create Tweet


Client.create_tweet(*, direct_message_deep_link=None, for_super_followers_only=None, place_id=None, media_ids=None, media_tagged_user_ids=None, poll_duration_minutes=None, poll_options=None, quote_tweet_id=None, exclude_reply_user_ids=None, in_reply_to_tweet_id=None, reply_settings=None, text=tweet, user_auth=True)
