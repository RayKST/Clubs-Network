import mysql.connector
from flask import Flask, render_template

# Database 

connection = mysql.connector.connect(
    host='localhost',
    database='python',
    user='root',
    password='')

cursor = connection.cursor()
cursor.close()
connection.close()


# Flask
app = Flask(__name__)

#Routes
@app.route("/")
def index():
    return render_template("index.html")