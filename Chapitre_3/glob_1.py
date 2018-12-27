#!/usr/bin/env python3
import glob


def main():
    fichier_conf_m = glob.glob("/etc/m*.conf")
    for fichier in fichier_conf_m:
        print(fichier)


if __name__ == "__main__":
    main()
