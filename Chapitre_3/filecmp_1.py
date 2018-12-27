#!/usr/bin/env python3
import filecmp


def main():
    f1 = "/etc/passwd"
    f2 = "/etc/group"
    q = "f1 est-il similaire à f2 ?"
    print(q)
    print(filecmp.cmp(f1, f2))
    print("f1 = " + f1)
    print("f2 = " + f2)


if __name__ == "__main__":
    main()
