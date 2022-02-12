from random import choice

from flask import Flask, request, render_template

import kadaiA1

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/omikuji/")
def omikuji():
    omikuji = ["大吉", "吉", "小吉"]
    result = choice(omikuji)
    return render_template("three_choice.html", result=result)


@app.route("/members/")
def members():
    members = ["Bob", "Tom", "Ken"]
    return render_template("members.html", members=members)

@app.route("/login/")
def login():
    return render_template("login.html", login=login)




if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)
