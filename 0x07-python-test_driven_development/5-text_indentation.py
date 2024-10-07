#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_space = False
    for let in text:
        if skip_space and let == " ":
            continue
        skip_space = False
        if let != "." and let != ":" and let != "?":
            print("{}".format(let), end="")
        else:
            print("{}".format(let))
            print()
            skip_space = True
