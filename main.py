from GoogleAPI import gcpNLP
from Streaming import StdOutListener

def main():
    obj = StdOutListener()                          # Creating object of Tweeter streaming class
    keywords = ["obama"]                            # Keyword list to filter tweets from streaming
    obj.streamer(keywords)                          # Stream the tweets

if __name__ == "__main__": 
    # calling main function 
    main()