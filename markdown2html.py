#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        bold = {"tag": False, "count": 0, "idx": 0}
        tags = ["*", "-", "#", "\n"]
        ul = False
        ol = False
        p = False
        file = open(sys.argv[1], "r")
        file_len = open(sys.argv[1], "r")
        html = open(sys.argv[2], "w")
        html_arr = [""]
        l = len(file_len.readlines())
        for (fidx, line) in enumerate(file):
            bold["boldidx"] = 0
            bold["count"] = 0
            bold["tag"] = False
            modifline = ""
            for (idx, char) in enumerate(line):
                if char == "*":
                    bold["count"] += 1
                if bold["count"] == 2 and not bold["tag"]:
                    bold["boldidx"] = idx
                    bold["tag"] = True
                    bold["count"] = 0
                if bold["count"] == 2 and bold["tag"]:
                    bidx = bold["idx"]
                    modifline = f"{line[:bidx-1]}<b>{line[bidx+1:idx-1]}</b>{line[idx+1:]}"
                    print(html)
                    bold["tag"] = False
                    bold["count"] = 0
                if char.isspace() and idx == 0:
                    if ul:
                        print(f"</ul>", file=html)
                        ul = False
                    if ol:
                        print(f"</ol>", file=html)
                        ol = False
                if char == " " and line[idx-1] == "#":
                    print(f"<h{idx}>{line[idx:-1]}</h{idx}>", file=html)
                if char == " " and line[idx-1] == "-":
                    if ul is False:
                        print(f"<ul>", file=html)
                        ul = True
                    print(f"<li>{line[idx+1:-1]}</li>", file=html)
                    if fidx + 1 == l and ul:
                        print(f"</ul>", file=html)
                        ul = False
                if char == " " and line[idx-1] == "*":
                    if ol is False:
                        print(f"<ol>", file=html)
                        ol = True
                    print(f"<li>{line[idx+1:-1]}</li>", file=html)
                    if fidx + 1 == l and ol:
                        print(f"</ol>", file=html)
                        ol = False
                if char.isspace() and p and idx == 0:
                    print("</p>", file=html)
                    p = False
                if char not in tags and idx == 0:
                    if p:
                        print("<br/>", file=html)
                    if p is False:
                        print(f"<p>", file=html)
                        p = True
                    print(f"{line}", file=html)
                    if fidx + 1 == l and p:
                        print("</p>", file=html)
                # Send modif
                if len(line) == idx + 1:
                    print(f"{modifline}")

        exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
