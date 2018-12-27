import urwid


liste_choix = [
    'Paris',
    'Marseille',
    'Lyon',
    'Lille',
    'Nice'
]


def menu(title, choix):
    contenu = [urwid.Text(title), urwid.Divider()]
    for c in choix:
        bouton = urwid.Button(c)
        urwid.connect_signal(bouton, 'click', selection, c)
        contenu.append(urwid.AttrMap(bouton, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(contenu))


def selection(bouton, choice):
    response = urwid.Text('Votre sélection: {}\n'.format(choice))
    done = urwid.Button('Valider')
    urwid.connect_signal(done, 'click', sortie)
    padding.original_widget = urwid.Filler(
        urwid.Pile(
            [response, urwid.AttrMap(done, None)]
        )
    )


def sortie(bouton):
    raise urwid.ExitMainLoop()


if __name__ == '__main__':
    padding = urwid.Padding(
        menu('Votre ville préférée ?', liste_choix), left=2, right=2)
    overlay = urwid.Overlay(
        padding, urwid.SolidFill('.'),
        align='center', width=('relative', 60),
        valign='middle', height=('relative', 60),
        min_width=20, min_height=9
    )
    main = urwid.MainLoop(overlay, palette=[('reversed', 'standout', '')])
    main.run()
