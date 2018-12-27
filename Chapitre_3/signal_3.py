#!/usr/bin/env python3
import signal
import time


def signal_alarm(signum, stack):
    print("Alarme reçue !")


def main():
    signal.signal(signal.SIGALRM, signal_alarm)
    signal.alarm(3)

    print("Simulation d'un traitement de 10 secondes...")
    time.sleep(10)
    print("Fin.")


if __name__ == "__main__":
    main()
