#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        file = open(sys.argv[1], "r")
        html = open(sys.argv[2], "w")
        for line in file:
            for (idx, char) in enumerate(line):
                if char == " " and line[idx-1] == "#":
                    print(f"<h{idx}>{line[idx:-1]}</h{idx}>", file=html)

        exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
