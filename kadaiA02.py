from random import choice

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


# str1 = input('1個目:')
# str2 = input('2個目:')
# str3 = input('3個目:')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # リクエストメソッドGETのときは以下の処理を行う
    if request.method == "GET":
        return '''
        <form action="/login" method="post">
            Password:<input type="text"><br>
            <input type='submit'>
        </from>
        '''


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/three_choice1/", methods=['GET'])
def three_choice1():
    return render_template("three_choice1.html")


@app.route("/three_choice1/", methods=['POST'])
def three_choice2():
    three_choice1 = [request.form['name1'], request.form['name2'], request.form['name3']]

    print(three_choice1)

    result = choice(three_choice1)
    return redirect(url_for('three_choice1', result=result))
    return render_template("three_choice1.html", result=result)


#
#
# @app.route("/three_choice1", methods=["GET", "POST"])
# def three_choice1():
#     print(request.form[str1, str2, str3])
#     if request.method == "GET":
#         return '''
#         <form action="/three_choice1" method="post">
#             1個目:<input type="text"><br>
#             2個目:<input type="text"><br>
#             3個目:<input type="text"><br>
#             <input type='submit'>
#         </from>
#         '''

@app.route("/members/")
def members():
    members = ["Bob", "Tom", "Ken"]
    return render_template("members.html", members=members)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=False)
