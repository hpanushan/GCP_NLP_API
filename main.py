from GoogleAPI import gcpNLP
from Streaming import StreamingClass

import re

def cleanTweet(tweet):
    # Removing links and mentions in tweet text 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())

def main():
    testTweet = "@libertlady @TheGreySonof @sergiolpn @EugeniaRolon_ @Angelalerena Correcci├│n; Foxconn tiene denuncias por trabajo eΓÇª https://t.co/XAuqim69GT"
    cleanedTestTweet = cleanTweet(testTweet)
    print(cleanedTestTweet)
    # Using Google Cloud Platform NLP model
    testTweetSentiment = gcpNLP(testTweet)
    cleanedTestTweetSentiment = gcpNLP(cleanedTestTweet)

    # Printing the results
    print("testTweetSentiment",testTweetSentiment)
    print("cleanedTestTweetSentiment",cleanedTestTweetSentiment)

if __name__ == "__main__": 
    # calling main function 
    main()

