from GoogleAPI import gcpNLP
from Streaming import StreamingClass

def main():
    obj = StreamingClass("Obama",2)                          # Creating object of Tweeter streaming class
    print(obj.getTweetId())

if __name__ == "__main__": 
    # calling main function 
    main()