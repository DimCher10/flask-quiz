from flask import Flask, render_template
from random import randint

app = Flask(__name__)
@app.route("/")
def index():
    num = randint(1,6)
    return render_template("index.html", num = num)


