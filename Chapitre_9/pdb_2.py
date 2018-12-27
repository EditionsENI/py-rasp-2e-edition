#!/usr/bin/env python3
import pdb


def explosion(arg="kaboom!", elem=1):
    elem = elem + 1
    return elem / 0


def main():
    for i in range(5):
        if i == 3:
            pdb.set_trace()
            explosion(elem=i)


if __name__ == "__main__":
    main()
