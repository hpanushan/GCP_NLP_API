from __future__ import absolute_import, print_function
from tweepy import OAuthHandler, Stream, StreamListener
import json

from GoogleAPI import gcpNLP
import Credentials

class StdOutListener(StreamListener):

    def on_data(self, data):
        dict_data = json.loads(data)                # Convert json object into dictionary object
        tweet_text = dict_data["text"]              # Filter the text field from tweet object
        sentiment = gcpNLP(tweet_text)              # Apply GCP NLP API method to tweet text
        print(sentiment)
        return True

    def on_error(self, status):
        print(status)

    def streamer(self):
        auth = OAuthHandler(Credentials.CONSUMER_KEY, Credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, self)
        stream.filter(track=['obama'])

