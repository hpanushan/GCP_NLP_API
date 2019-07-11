import tweepy
import Credentials
import json
 
class StreamingClass():

    def returnTweets(self,keyword="obama",n=10):
        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
 
        # creation of the actual interface, using authentication
        api = tweepy.API(auth)

        search = tweepy.Cursor(api.search, q=keyword, result_type="recent").items(n)

        return search     

    def getUserName(self):
        # The method to get user name of each  tweet object
        iterabeTweetObject = self.returnTweets()
        for i in iterabeTweetObject:
            print(i.user.screen_name)

    def getTweetText(self):
        # The method to get tweet text of tweet objects
        tweetText = []
        iterabeTweetObject = self.returnTweets()
        for i in iterabeTweetObject:
            tweetText.append(i.text)
        return tweetText

obj = StreamingClass()
print(obj.getUserName())
