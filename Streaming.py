import tweepy
import Credentials
import json
 
class StreamingClass():
    #keyword = "obama"
    #n = 10
    def __init__(self,keyword,n):
        
        self.keyword = keyword
        self.n = n
        self.search = ""

    def authentication(self):
        auth = tweepy.OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
        api  = tweepy.API(auth)
        return api
    
    def findTweets(self):
        self.search = tweepy.Cursor(self.authentication().search, q=self.keyword, result_type="recent").items(self.n)

    def getDetails(self):
        # The method to get tweet id 
        tweetID = []
        tweetUserName = []
        tweetText = []
        iterabeTweetObject = self.search
        for i in iterabeTweetObject:
            tweetID.append(i.id_str)
            tweetUserName.append(i.user.screen_name)
            tweetText.append(i.text)
        return tweetID,tweetUserName,tweetText



