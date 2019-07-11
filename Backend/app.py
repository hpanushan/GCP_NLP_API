from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def getValue():
    filter = request.args.get('filter')
    return filter


if __name__ == '__main__':
    app.run(debug=True)
