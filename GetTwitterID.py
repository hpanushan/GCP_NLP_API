from tweepy import OAuthHandler, Stream, StreamListener
import tweepy
import Credentials

def getTwitterID(screen_name):
    auth = tweepy.OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    userID = api.get_user(screen_name)

    return userID.id
    
