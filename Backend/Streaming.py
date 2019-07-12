import tweepy
import Credentials
import json
 
class StreamingClass():
    #keyword = "obama"
    #n = 10
    def __init__(self,keyword,n):
        # Constructor to define class variables
        self.keyword = keyword
        self.n = n
        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
 
        # creation of the actual interface, using authentication
        api = tweepy.API(auth)

        self.search = tweepy.Cursor(api.search, q=self.keyword, result_type="recent").items(self.n)

    def getTweetId(self):
        # The method to get tweet id 
        tweetID = []
        iterabeTweetObject = self.search
        for i in iterabeTweetObject:
            tweetID.append(i.id_str)
        return tweetID

    def getUserName(self):
        # The method to get user name of each  tweet object
        tweetUserName = []
        iterabeTweetObject = self.search
        for i in iterabeTweetObject:
            tweetUserName.append(i.user.screen_name)
        return tweetUserName

    def getTweetText(self):
        # The method to get tweet text of tweet objects
        tweetText = []
        iterabeTweetObject = self.search
        for i in iterabeTweetObject:
            tweetText.append(i.text)
        return tweetText


