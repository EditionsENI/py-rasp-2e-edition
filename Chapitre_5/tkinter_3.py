#!/usr/bin/env python3
from tkinter import Tk


LARGEUR = 400
HAUTEUR = 300


def main():
    fenetre = Tk()
    largeur_div = (fenetre.winfo_screenwidth() - LARGEUR) // 2
    hauteur_div = (fenetre.winfo_screenheight() - HAUTEUR) // 2
    dimensions = '{f_x}x{f_y}+{p_x}+{p_y}'.format(
        f_x=LARGEUR,
        f_y=HAUTEUR,
        p_x=largeur_div,
        p_y=hauteur_div
    )
    fenetre.geometry(dimensions)
    fenetre.mainloop()


if __name__ == '__main__':
    main()
