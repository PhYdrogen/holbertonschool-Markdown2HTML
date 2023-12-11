#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        ul = False
        file = open(sys.argv[1], "r")
        file_len = open(sys.argv[1], "r")
        html = open(sys.argv[2], "w")
        l = len(file_len.readlines())
        for (fidx, line) in enumerate(file):
            for (idx, char) in enumerate(line):
                if char == " " and line[idx-1] == "#":
                    print(f"<h{idx}>{line[idx:-1]}</h{idx}>", file=html)
                    ul = False
                if char == " " and line[idx-1] == "-":
                    if ul is False:
                        print(f"<ul>", file=html)
                        ul = True
                    print(f"<li>{line[idx+1:-1]}</li>", file=html)
                    if fidx + 1 == l and ul is True:
                        print(f"</ul>", file=html)

        exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
