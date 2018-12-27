#!/usr/bin/env python3
from flask import render_template
from flask import request
from flask import Flask


app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template("flask_4_echo.html")


@app.route("/echo", methods=["POST"])
def echo():
    return render_template("flask_4_echo.html", texte=request.form["texte"])


if __name__ == '__main__':
    app.run()
