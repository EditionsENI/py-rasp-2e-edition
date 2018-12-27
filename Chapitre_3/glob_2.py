#!/usr/bin/env python3
import glob


def main():
    fichiers_conf = glob.glob("/etc/**/**")
    for fichier in fichiers_conf:
        print(fichier)


if __name__ == "__main__":
    main()
