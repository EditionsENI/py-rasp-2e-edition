#!/usr/bin/env python3
from lcd16x2 import LCD16x2
import time
import cmd


class LCmD(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ">> "
        self.intro = "Bienvenue dans LCmD!"
        self.lcd = LCD16x2()

    def do_ecrire(self, ligne):
        """Écrit un message dans l'écran du LCD."""
        self.lcd.write_string(ligne)

    def do_nettoyer(self, ligne):
        """Nettoie les caractères du LCD."""
        self.lcd.clear()

    def do_EOF(self, ligne):
        self.lcd.close(clear=True)
        print("Merci d'avoir utilisé LCmD!")
        return -1

    def do_quitter(self, ligne):
        """Ferme le menu."""
        return self.do_EOF(ligne)


if __name__ == "__main__":
    LCmD().cmdloop()
