#!/usr/bin/env python3
from xml.etree import ElementTree


def main():
    with open("bdd/commandes.xml", "r", encoding="UTF-8") as f:
        xml = ElementTree.parse(f)
        racine = xml.getroot()
    commandes = racine.find("commandes")
    print("Nombre de noeuds dans le noeud 'commandes': {}".format(len(commandes)))
    for commande in commandes:
        print("""  Nom: {}
  Code: {}
  Quantite: {}""".format(
      commande.text.strip(),
      commande.attrib["code"],
      commande.attrib["quantite"]
    )
)


if __name__ == "__main__":
    main()
