#!/usr/bin/env python3
import urwid
import time


class Horloge:
    def __init__(self):
        self.configurer_horloge()
        self.palette = [('horloge', 'dark blue', '')]
        self.boucle = urwid.MainLoop(
            self.horloge,
            palette=self.palette,
            unhandled_input=self.quitter)
        self.boucle.set_alarm_in(1, self.actualiser)

    def actualiser(self, boucle=None, data=None):
        self.configurer_horloge()
        boucle.widget = self.horloge
        boucle.set_alarm_in(1, self.actualiser)

    def configurer_horloge(self):
        text = time.strftime('%H:%M:%S')
        font = urwid.font.HalfBlock7x7Font()
        self.texte_horloge = urwid.BigText(text, font)
        self.horloge = urwid.Filler(
            urwid.AttrMap(
                urwid.Padding(
                    self.texte_horloge,
                    'center',
                    width='clip'
                ), 'horloge'
            ), 'middle'
        )

    def demarrer(self):
        self.boucle.run()

    def quitter(self, touche):
        if touche in ('q', 'Q'):
            raise urwid.ExitMainLoop()


if __name__ == '__main__':
    horloge = Horloge()
    horloge.demarrer()
