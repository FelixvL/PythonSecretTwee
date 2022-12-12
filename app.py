from flask import Flask
from decouple import config

app = Flask(__name__)



@app.route("/")
def hello_world():
    VANMIJGEHEIM = config('OOGEHEIM')
    geheim = VANMIJGEHEIM
#    geheim = 'hoi'
    return "<p>Hello, World!</p>" + geheim