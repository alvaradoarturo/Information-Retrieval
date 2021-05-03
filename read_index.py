#!/usr/bin/python3

import ast
import os
import sys
from parsing import parsing_input


def main():
    args = sys.argv[1:]
    if(args[0] == "--doc"):
        print("Loading relevant document information:")
        print("Listing for document: " + args[1])
        parsing_input(args[1])
    elif(len(args) > 2):
        print("Loading relevant term information inside specified document")
    elif(args[0] == "--term"):
        print("Loading relevant term information")
    else:
        print("Error paring input")


if __name__ == '__main__':
    main()
