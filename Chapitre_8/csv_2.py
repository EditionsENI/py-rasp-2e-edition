#!/usr/bin/env python3
import csv


def main():
    chemin = "bdd/fichier.csv"
    print("Lecture de '{}'...".format(chemin))
    with open(chemin, 'r') as f:
        reader = csv.reader(f)
        for ligne in reader:
            print("## Ligne courante: {}".format(ligne))
            print("# 3ème colonne: {}".format(ligne[2]))
    print("OK!")


if __name__ == "__main__":
    main()
