#!/usr/bin/env python3
from flask import render_template
from flask import redirect
from flask import Flask


app = Flask(__name__)


@app.route('/')
def accueil():
    return redirect("/article/10")


@app.route('/article/<int:art>')
def afficher_article(art):
    return render_template('flask_3_art.html', art=art)


if __name__ == '__main__':
    app.run()
