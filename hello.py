#inja

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hallo():
    message = "hello world"
    return render_template('test.html')
