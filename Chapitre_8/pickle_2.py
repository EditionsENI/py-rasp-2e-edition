#!/usr/bin/env python3
import pickle


def main():
    chemin = "bdd/pickle.db"
    print("Lecture de '{}'...".format(chemin))
    with open(chemin, "rb") as f:
        obj = pickle.load(f)
    print("Type de l'objet: {}".format(type(obj)))
    print("__str__ sur l'objet: {}".format(obj))


if __name__ == "__main__":
    main()
