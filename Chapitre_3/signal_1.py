#!/usr/bin/env python3
import signal
import time
import sys
import os


def signal_sigusr1(num_signal, pile):
    print("Signal SIGUSR1 reçu!")


def signal_sigint(num_signal, pile):
    print("SIGINT reçu! Fermeture du programme.")
    sys.exit(num_signal)


def main():
    signal.signal(signal.SIGUSR1, signal_sigusr1)
    signal.signal(signal.SIGINT, signal_sigint)

    print("Quel est mon PID ?", os.getpid())

    while True:
        time.sleep(1)
        print("En attente d'un signal ...")


if __name__ == "__main__":
    main()
