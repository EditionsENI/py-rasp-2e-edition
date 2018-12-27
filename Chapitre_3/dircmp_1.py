#!/usr/bin/env python3
import filecmp


def main():
    d1 = "/tmp"
    d2 = "/var/tmp"
    dcmp = filecmp.dircmp(d1, d2)
    dcmp.report()


if __name__ == "__main__":
    main()

