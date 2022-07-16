import mysql.connector
from flask import Flask, render_template, redirect, request, url_for

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
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['USERNAME']
        password = request.form['PASSWORD']
        return redirect(url_for("main"))
    else:
        return render_template("login.html")

@app.route("/main", methods=["GET"])
def main():
    return render_template("main.html")