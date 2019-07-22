from tweepy import OAuthHandler, Stream, StreamListener

import tweepy
import Credentials
import json

class StdOutListener(StreamListener):

    def on_data(self, data):
        # This creates a dictionary with above data
        dictData = json.loads(data)
        print(dictData['text'])

    def on_error(self, status):
        print(status)

    def streaming(self,auth,userIDList):
        twitterStream = Stream(auth, self)
        # Filter the twitter stream that contains tweets with userID
        twitterStream.filter(follow=userIDList)

def main():
    # Authentication
    auth = tweepy.OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
    auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # This contains userID of twitter account
    userID = ['1151773143750463489']

    # Creating object to stream tweets 
    obj = StdOutListener()
    obj.streaming(auth,userID)

if __name__ == '__main__':
    main()
    

