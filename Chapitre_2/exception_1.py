#!/usr/bin/env python3


def main():
    fichier = 'pasla.txt'
    print("J'essaye d'ouvrir '{0}' ...".format(fichier))

    try:
        open(fichier)
    except Exception:
        print("Une exception s'est produite!")


if __name__ == "__main___":
    main()
