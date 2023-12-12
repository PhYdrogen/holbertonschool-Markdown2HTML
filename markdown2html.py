#!/usr/bin/python3
""" This file is made to parse some Markdown to HTML """

import sys
import hashlib


"""
Test comment
Test comment
Test comment
"""


def remove_prefix(self: str, prefix: str) -> str:
    """
    Test comment
    Test comment
    Test comment
    """
    if self.startswith(prefix):
        return self[len(prefix):]
    else:
        return self[:]


"""
Test comment
Test comment
Test comment
"""


def remove_suffix(self: str, suffix: str) -> str:
    """
    Test comment
    Test comment
    Test comment
    """
    if suffix and self.endswith(suffix):
        return self[:-len(suffix)]
    else:
        return self[:]


def main():
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    try:
        tags = ["*", "-", "#", "\n"]
        ul = False
        ol = False
        p = False
        file = open(sys.argv[1], "r")
        file_len = open(sys.argv[1], "r")
        html = open(sys.argv[2], "w")
        longeur = len(file_len.readlines())
        for (fidx, line) in enumerate(file):
            if line.find("((") != -1 and line.find("))") != -1:
                find = line.find('((')
                rfind = line.rfind('))')
                word = line[find+2:rfind]
                word = word.replace("C", "")
                word = word.replace("c", "")
                line = line.replace(f"(({line[find+2:rfind]}))", word)
                line += "\n"
            if line.find("[[") != -1 and line.find("]]") != -1:
                find = line.find('[[')
                rfind = line.rfind(']]')
                word = line[find+2:rfind]
                secret = hashlib.md5(word.encode()).hexdigest()
                line = line.replace(f"{line[find:rfind+2]}", secret, 1)
                line += "\n"
            if line.find("**") != -1:
                line = line.replace("**", "<b>", 1)
                line = line.replace("**", "</b>", 1)
            if line.find("__") != -1:
                line = line.replace("__", "<em>", 1)
                line = line.replace("__", "</em>", 1)
            if line[0] not in tags:
                if p:
                    print("<br>", file=html)
                if not p:
                    print(f"<p>", file=html)
                    p = True
                print(f"{line[:-1]}", file=html)
            if line.isspace():
                if ul:
                    print("</ul>", file=html)
                    ul = False
                if ol:
                    print("</ol>", file=html)
                    ol = False
                if p:
                    print("</p>", file=html)
                    p = False
            if line.rfind("#") != -1:
                pos = line.rfind("#")
                line = line.remove_prefix(f"{line[:pos+2]}")
                line = f"<h{pos+1}>{line[:-1]}</h{pos+1}>"
                print(line, file=html)
            if line.startswith("-"):
                if ul is False:
                    tag = f"<ul>"
                    ul = True
                    print(tag, file=html)
                line = line.remove_prefix("- ")
                line = f"<li>{line[:-1]}</li>"
                print(line, file=html)
            if line.startswith("*"):
                if ol is False:
                    tag = f"<ol>"
                    ol = True
                    print(tag, file=html)
                line = line.remove_prefix("* ")
                line = f"<li>{line[:-1]}</li>"
                print(line, file=html)
            if fidx + 1 == longeur:
                if ol:
                    print("</ol>", file=html)
                    ol = False
                if ul:
                    print("</ul>", file=html)
                    ul = False
                if p:
                    print("</p>", file=html)
                    p = False

        exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()
