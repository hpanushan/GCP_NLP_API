import twitter
import Credentials

def getTwitterID(screenName):
    t = twitter.Twitter(auth=twitter.OAuth(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET, Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET))
    response = t.users.lookup(screen_name=screenName)
    responseList = list(response)

    return responseList[0]['id']