from flask import Flask, jsonify, request, render_template
from Streaming import StreamingClass
from GoogleAPI import gcpNLP

import os
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def getValue():
    filter = request.args.get('filter')         # Keyword
    
    # Calling the streaming class
    obj = StreamingClass(filter,10)

    # Tweet data list
    tweetIDList = obj.getTweetId()              # Tweet ID list
    tweetUserNameList = obj.getUserName()       # User name list
    tweetTextList = obj.getTweetText()          # Tweet text list
    sentimentList = []                          # Sentiment list

    # Getting the sentiment value of tweets
    for i in tweetTextList:
        sentimentList.append(gcpNLP(i))

    dataDictionary = {}
    for i in range(0,len(sentimentList)):
        data = {}                               # For one column
        data['id'] = tweetIDList[i]
        data['user_name'] = tweetUserNameList[i]
        data['text'] = tweetTextList[i]
        data['sentiment_score'] = sentimentList[i]
        dataDictionary[str(i)] = data

    jsonData = json.dumps(dataDictionary)

    return render_template('index.html', analysis=jsonData)

if __name__ == '__main__':
    app.run(debug=True)
