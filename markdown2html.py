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
        l = len(file_len.readlines())
        for (fidx, line) in enumerate(file):
            if line.isspace():
                if ul:
                    print("</ul>", file=html)
                    ul = False
                if ol:
                    print("</ol>", file=html)
                    ol = False
            if line.rfind("#") != -1:
                pos = line.rfind("#")
                line = line.removeprefix(f"{line[:pos+2]}")
                line = f"<h{pos+1}>{line[:-1]}</h{pos+1}>"
                print(line, file=html)
            if line.startswith("-"):
                if ul is False:
                    tag = f"<ul>"
                    ul = True
                    print(tag, file=html)
                line = line.removeprefix("- ")
                line = f"<li>{line[:-1]}</li>"
                print(line, file=html)
                if ul and fidx + 1 == l:
                    print("</ul>", file=html)
                    ul = False
            if line.startswith("*"):
                if ol is False:
                    tag = f"<ol>"
                    ol = True
                    print(tag, file=html)
                line = line.removeprefix("* ")
                line = f"<li>{line[:-1]}</li>"
                print(line, file=html)
                if ol and fidx + 1 == l:
                    print("</ol>", file=html)
                    ol = False

                # print(line)
            # bold["boldidx"] = 0
            # bold["count"] = 0
            # bold["tag"] = False

            # for (idx, char) in enumerate(line):
            #     if char == "*":
            #         bold["count"] += 1
            #     if bold["count"] == 2 and not bold["tag"]:
            #         bold["boldidx"] = idx
            #         bold["tag"] = True
            #         bold["count"] = 0
            #     if bold["count"] == 2 and bold["tag"]:
            #         bidx = bold["idx"]
            #         html_arr.append(f"<b>{line[bidx+1:idx-1]}</b>")
            #         bold["tag"] = False
            #         bold["count"] = 0
            #     if char.isspace() and idx == 0:
            #         if ul:
            #             html_arr.append("</ul>")
            #             ul = False
            #         if ol:
            #             html_arr.append("</ol>")
            #             ol = False
            #     if char == " " and line[idx-1] == "#":
            #         html_arr.append(f"<h{idx}>{line[idx:-1]}</h{idx}>")
            #     if char == " " and line[idx-1] == "-":
            #         if ul is False:
            #             html_arr.append("<ul>")
            #             ul = True
            #         html_arr.append(f"<li>{line[idx+1:-1]}</li>")
            #         if fidx + 1 == l and ul:
            #             html_arr.append("</ul>")
            #             ul = False
            #     if char == " " and line[idx-1] == "*" and not bold["tag"]:
            #         if ol is False:
            #             html_arr.append("<ol>")
            #             ol = True
            #         html_arr.append(f"<li>{line[idx+1:-1]}</li>")
            #         if fidx + 1 == l and ol:
            #             html_arr.append("</ol>")
            #             ol = False
            #     if char.isspace() and p and idx == 0:
            #         html_arr.append("</p>")
            #         p = False
            #     if char not in tags and idx == 0:
            #         if p:
            #             html_arr.append("</br>")
            #         if p is False:
            #             html_arr.append("<p>")
            #             p = True
            #         html_arr.append(line)
            #         if fidx + 1 == l and p:
            #             html_arr.append("</p>")
                # Send modif
        exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
