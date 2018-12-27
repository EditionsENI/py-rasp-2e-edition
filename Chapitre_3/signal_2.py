#!/usr/bin/env python3
import signal
import sys
import os


def sortir_sigusr1(num_signal, pile):
    sys.exit("Signal USR1 reçu ! Au revoir !")


def main():
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGUSR1, sortir_sigusr1)
    print("Quel est mon PID ?", os.getpid())
    signal.pause()


if __name__ == "__main__":
    main()
