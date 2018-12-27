#!/usr/bin/env python3
from PIL import Image


def main():
   image = 'images/hello_1.png'
   resultat = 'images/hello_4.png'
   img = Image.open(image)
   nouvelletaille = (100, 0, 300, 200)
   res = img.crop(nouvelletaille)
   res.save(resultat)


if __name__ == '__main__':
    main()
