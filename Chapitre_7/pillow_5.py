#!/usr/bin/env python3
from PIL import ImageOps
from PIL import Image


def main():
    image = 'images/hello_1.png'
    resultat = 'images/hello_5.png'
    img = Image.open(image)
    res = ImageOps.flip(img)
    res.save(resultat)


if __name__ == '__main__':
    main()
