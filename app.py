from flask import Flask, jsonify, request, render_template
from Streaming import StreamingClass
from GoogleAPI import gcpNLP
from main import main

import tweepy
import os
import json

app = Flask(__name__)

@app.route('/')
def renderIndex():
    return render_template('index.html')

@app.route('/getValue', methods=['POST'])
def getValue():
    filter = request.form['filter']
    
    obj = StreamingClass("obama",2)
    obj.findTweets()

    # Tweets data
    tweetIDList,tweetUserNameList,tweetTextList = obj.getDetails()
    ##### 
    
    # Covert into JSON data format
    dataDictionary = {}
    for i in range(0,len(tweetIDList)):
        row = {}
        row["id"] = tweetIDList[i]
        row["userName"] = tweetUserNameList[i]
        row["text"] = tweetTextList[i]
        dataDictionary[str(i)] = row

    jsonData = json.dumps(dataDictionary)
    print(jsonData)
    
    return render_template('index.html',analysis=jsonData)

if __name__ == '__main__':
    app.run(debug=True)
