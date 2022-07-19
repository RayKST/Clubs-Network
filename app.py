# Imports
import mysql.connector
from flask import Flask, render_template, redirect, request, url_for
from db.functions import CheckUser, CreateUser


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
            return redirect(url_for("main"))        # If CreckUser == True go to main page
        else:
            return redirect(url_for("login"))       # Else back to login page
            
    else:
        return render_template("login.html")


@app.route("/main", methods=["GET"])
def main():
    return render_template("main.html")


@app.route("/create-user", methods = ["GET", "POST"])
def create_user ():
    if request.method == "POST":
        username = request.form['USERNAME']
        password = request.form['PASSWORD']
        createUser = CreateUser(username, password, cursor, connection)
        
        if createUser == True:
            return redirect(url_for("login"))       # If CreateUser function == True go to login page
        else:
            return redirect(url_for("create-user")) # Else back to create-user page

    else:
        return render_template("create-user.html")