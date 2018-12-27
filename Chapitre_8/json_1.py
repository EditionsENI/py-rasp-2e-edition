#!/usr/bin/env python3
import json


def main():
    donnees = {
        "Renault": {
            "Clio": {
                "annee": 1999,
                "version": 1,
                "prix": 1000,
                "devise": "EUR"
            }
        },
        "Peugeot": {
            "206": {
                "annee": 2004,
                "version": [2, 3],
                "prix": 2000,
                "devise": "EUR"
            }
        }
    }
    json_str = json.dumps(donnees, sort_keys=True, indent=4)
    print(json_str)
    with open('./voitures.json', 'w') as voitures_json:
        voitures_json.write(json_str)


if __name__ == '__main__':
    main()
