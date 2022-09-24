from colorama import Cursor
from flask import Flask, render_template
from random import randint
import sqlite3 

app = Flask(__name__)
@app.route("/")
def index():
    connection = sqlite3.connect("historyBot.sqlite3")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks") 
    result = cursor.fetchall()
    print(result)
    return render_template("index.html", result = result)
app.run()
    
 
     

