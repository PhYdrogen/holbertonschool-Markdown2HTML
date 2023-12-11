#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    try:
        file = open("README.md")
        exit(0)
    except:
        print("Missing <filename>")


if __name__ == "__main__":
    main()
