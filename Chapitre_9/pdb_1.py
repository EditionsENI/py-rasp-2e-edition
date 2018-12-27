#!/usr/bin/env python3


def explosion(arg="kaboom!", elem=1):
    elem = elem + 1
    raise Exception(arg)


def main():
    for i in range(5):
        if i == 3:
            explosion("boom!")


if __name__ == "__main__":
    main()
