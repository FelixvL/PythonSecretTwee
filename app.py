from flask import Flask
import os

app = Flask(__name__)



@app.route("/")
def hello_world():
    VANMIJGEHEIM = os.environ['OOGEHEIM']
    geheim = VANMIJGEHEIM
#    geheim = 'hoi'
    return "<p>Hello, World!</p>" + geheim