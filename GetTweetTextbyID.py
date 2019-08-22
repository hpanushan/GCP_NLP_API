from Credentials import *
import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = api.statuses_lookup(['1159286092433980000']) # id_list is the list of tweet ids
tweet_txt = []
for i in tweets:
    tweet_txt.append(i.text)

print(tweet_txt)