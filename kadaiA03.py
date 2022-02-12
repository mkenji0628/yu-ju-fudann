from random import choice

from flask import Flask, request, render_template

app = Flask(__name__)

str1 = input('1:')
str2 = input('2個目:')
str3 = input('3個目:')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/omikuji")
def omikuji():
    omikuji = [str, "吉", "小吉"]
    result = choice(omikuji)
    return render_template("omikuji.html", result=result)


@app.route("/members/")
def members():
    members = ["Bob", "Tom", "Ken"]
    return render_template("members.html", members=members)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=False)
