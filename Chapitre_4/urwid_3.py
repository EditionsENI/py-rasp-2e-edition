#!/usr/bin/env python3
import urwid
import os


class NavigateurFichiers(urwid.WidgetPlaceholder):
    def __init__(self, chemin):
        self.chemin_courant = chemin
        self.chemin_prec = None
        self.liste_fichiers = sorted(os.listdir(self.chemin_courant))
        if self.chemin_courant != '/':
            self.liste_fichiers.insert(0, '..')
        super(NavigateurFichiers, self).__init__(self.creer_contenu())

    def maj_liste_fichiers(self, choix):
        if choix == '..':
            nouveau_chemin = os.path.dirname(self.chemin_courant)
        else:
            nouveau_chemin = os.path.join(self.chemin_courant, choix)

        if os.path.isdir(nouveau_chemin):
            self.chemin_prec = self.chemin_courant
            self.chemin_courant = nouveau_chemin

        self.liste_fichiers = sorted(os.listdir(self.chemin_courant))

        if self.chemin_courant != '/':
            self.liste_fichiers.insert(0, '..')

    def creer_contenu(self):
        contenu = []
        for fichier in self.liste_fichiers:
            bouton = urwid.Button(fichier)
            if os.path.isdir(os.path.join(self.chemin_courant, fichier)):
                urwid.connect_signal(
                    bouton, 'click', self.maj_contenu, fichier
                )
                contenu.append(urwid.AttrMap(
                    bouton, 'rep', focus_map='rep_focus')
                )
            else:
                contenu.append(urwid.AttrMap(
                    bouton, None, focus_map='fichier'))
        return urwid.AttrMap(
            urwid.LineBox(
                urwid.ListBox(
                    urwid.SimpleFocusListWalker(contenu)),
                self.chemin_courant), 'contenu'
        )

    def maj_contenu(self, bouton, choix):
        self.maj_liste_fichiers(choix)
        self.original_widget = self.creer_contenu()

    def quitter(self, touche):
        if touche in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def palette(self):
        return [
            ('contenu', 'light gray', 'light blue'),
            ('fichier', 'light gray', 'dark red'),
            ('rep_focus', 'white', 'dark red'),
            ('rep', 'black', 'light blue')
        ]


def main():
    nav = NavigateurFichiers(os.getcwd())
    main = urwid.MainLoop(
        nav,
        nav.palette(),
        unhandled_input=nav.quitter
    )
    main.run()


if __name__ == '__main__':
    main()
