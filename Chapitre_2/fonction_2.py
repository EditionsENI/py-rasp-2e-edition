#!/usr/bin/env python3


def args_variables(*args):
    print("Arguments? {0}".format(args))
    print("Type? {0}".format(type(args)))
    for index, arg in enumerate(args):
        print('Argument #{0}: {1}'.format(index, arg))


if __name__ == "__main__":
    args_variables([1, 2], 3, (4, 5), {'a': 'un', 'b': 'deux'})
