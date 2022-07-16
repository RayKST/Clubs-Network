import mysql.connector
from flask import Flask, render_template

# Database 

connection = mysql.connector.connect(
    host='localhost',
    database='clubs',
    user='root',
    password='')

#cursor = connection.cursor()
#cursor.close()
#connection.close()


# Flask
app = Flask(__name__)

#Routes
@app.route("/login")
def index():
    return render_template("login.html")