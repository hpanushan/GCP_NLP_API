from GoogleAPI import gcpNLP
from Streaming import StreamingClass

def main():
    obj = StreamingClass("Obama",10)                          # Creating object of Tweeter streaming class
    print(obj.getTweetText())

if __name__ == "__main__": 
    # calling main function 
    main()