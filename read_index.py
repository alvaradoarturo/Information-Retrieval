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
    if(args[0] == "--doc"):
        print("doc")
        parsing_input(args[1])
    elif(args[0] == "--term"):
        if(args[2] == "--doc"):
            print("Term inside doc")
        else:
            print("Just term ")
    else:
        print("Error paring input")


if __name__ == '__main__':
    main()
