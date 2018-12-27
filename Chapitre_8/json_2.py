#!/usr/bin/env python3
import json


def main():
    json_str = ""
    with open('./voitures.json', 'r') as voitures_json:
        for ligne in voitures_json.readlines():
            json_str += ligne.strip()
    donnees = json.loads(json_str)
    print(donnees)
    print(donnees["Renault"]["Clio"]["prix"])


if __name__ == '__main__':
    main()
