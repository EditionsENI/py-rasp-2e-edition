#!/usr/bin/env python3
import urwid


def main():
    # Passage en revue des widgets les plus basiques de la bibliothèque.
    # Le widget Edit est utilisé pour taper du texte dans un champ texte.
    champ_q = urwid.Edit('Quel est votre nom ? ')

    # Le widget Texte est utilisé pour afficher du texte dans un champ texte.
    # Ici, le champ est vide.
    champ_rep = urwid.Text('')

    # Le widget Button affiche un bouton.
    btn_sortir = urwid.Button('Sortir')

    # Le widget Divider créé un espace entre deux widgets.
    div = urwid.Divider()

    # Le widget Pile est un conteneur dans lequel plusieurs widgets sont
    # empilés verticalement.
    pile = urwid.Pile([champ_q, div, champ_rep, div, btn_sortir])

    # Le widget Filler est aussi un conteneur avec des prioriétés d'affichage
    # des widgets contenus. Ici, le widget Pile est ajouté à Filler avec un
    # alignement vertical en haut de la console (top).
    interface = urwid.Filler(pile, valign='top')

    # Deux fonctions handler sont définies et associées à des actions.
    def fct_reponse(bouton, ntexte):
        champ_rep.set_text('Bonjour {} !'.format(ntexte))

    def fct_sortir(bouton):
        raise urwid.ExitMainLoop()

    # La fonction connect_signal associe un changement d'état à un appel de
    # fonction.
    urwid.connect_signal(champ_q, 'change', fct_reponse)
    urwid.connect_signal(btn_sortir, 'click', fct_sortir)

    # Enfin, le widget MainLoop lance finalement le programme.
    main = urwid.MainLoop(interface)
    main.run()


if __name__ == '__main__':
    main()
