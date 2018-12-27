#!/usr/bin/env python3
import urwid


def sortie(touche):
    if touche in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def main():
    texte = urwid.Text('Hello world!')
    padding = urwid.Padding(texte, align='center', width='pack')
    interface = urwid.Filler(padding, valign='middle')
    main = urwid.MainLoop(interface, unhandled_input=sortie)
    main.run()


if __name__ == '__main__':
    main()
