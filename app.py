from flask import Flask, jsonify, request, render_template
from Streaming import StreamingClass
from GoogleAPI import gcpNLP
from LangTranslator import langTranslator

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

    keyword = "@" + str(filter)
    obj = StreamingClass(keyword,10)
    obj.findTweets()

    # Tweets data
    tweetIDList,tweetUserNameList,tweetTextList = obj.getDetails()
    ##### 
    # Covert into JSON data format
    
    dataList = []
    for i in range(0,len(tweetIDList)):
        row = {}
        row["id"] = tweetIDList[i]
        row["userName"] = tweetUserNameList[i]
        row["text"] = tweetTextList[i]
        try:
            row["sentiment"] = gcpNLP(tweetTextList[i])
        except: 
            row["sentiment"] = gcpNLP(langTranslator(tweetTextList[i]))
        #dataDictionary[str(i)] = row
        dataList.append(row)

    return render_template('index.html',analysis=dataList)

if __name__ == '__main__':
    app.run(debug=True)
