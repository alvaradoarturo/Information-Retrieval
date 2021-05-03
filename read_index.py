#!/usr/bin/python3

import ast
import os
import sys
from parsing import parsing_input


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    print(args[0])
    print(args[1])
    parsing_input(args[1])


if __name__ == '__main__':
    main()

