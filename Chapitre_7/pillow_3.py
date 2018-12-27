#!/usr/bin/env python3
from PIL import Image


def main():
    image = 'images/hello_1.png'
    resultat = 'images/hello_3.png'
    nouvelletaille = (300, 150)
    img = Image.open(image)
    res = img.resize(nouvelletaille)
    res.save(resultat)


if __name__ == '__main__':
    main()
