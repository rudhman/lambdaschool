from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/birthday")
def birthday():
    return "Jan 19 1997"

@app.route("/greeting/<name>")
def greeting(name):
    return "Hello {}".format(name)

@app.route("/add/<num1>/<num2>")
def add(num1, num2):
    return str(int(num1)+int(num2))

@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    return str(int(num1)*int(num2))


@app.route("/subtract/<int:num1>/<int:num2>")
def subtract(num1, num2):
    return str(int(num1)-int(num2))

@app.route("/favouritefoods")
def favouritefoods():
    list = ["noodels", "pineapple rice", "icecreams"]
    return jsonify(list)
