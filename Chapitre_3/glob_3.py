#!/usr/bin/env python3
import glob


def main():
    iter_fichiers = glob.iglob("/etc/m*.conf")
    print(type(iter_fichiers))
    print(next(iter_fichiers))


if __name__ == "__main__":
    main()
