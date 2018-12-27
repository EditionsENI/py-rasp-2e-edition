#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
def dit_hello():
    return "Hello World!"


@app.route("/user/<utilisateur>")
def affiche_utilisateur(utilisateur):
    return "Bonjour {} ! Comment allez-vous ?".format(utilisateur)


@app.route("/id/<int:numero>")
def affiche_id(numero):
    return "Identifiant #{}".format(numero)


@app.route("/path/<path:souschemin>")
def affiche_souschemin(souschemin):
    return "Quel est le sous-chemin ? {}".format(souschemin)


if __name__ == "__main__":
    app.run()
