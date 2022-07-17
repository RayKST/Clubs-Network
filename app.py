# Imports
import mysql.connector
from flask import Flask, render_template, redirect, request, url_for
from db.functions import CheckUser


# Database / Variables

connection = mysql.connector.connect(
        host='localhost',
        database='clubs',
        user='root',
        password='')

cursor = connection.cursor()

# Flask
app = Flask(__name__)

#Routes
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['USERNAME']
        password = request.form['PASSWORD']
        userInDatabse = CheckUser(username, password, cursor)
        
        if userInDatabse == True:
            return redirect(url_for("main"))
        else:
            return redirect(url_for("login"))
    else:
        return render_template("login.html")

@app.route("/main", methods=["GET"])
def main():
    return render_template("main.html")