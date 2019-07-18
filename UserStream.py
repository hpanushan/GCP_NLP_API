from tweepy import OAuthHandler, Stream, StreamListener

import tweepy
import Credentials

# Authentication
auth = tweepy.OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class StdOutListener(StreamListener):

    def on_data(self, data):
        # process stream data here
        print(data)

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=['988355810'])