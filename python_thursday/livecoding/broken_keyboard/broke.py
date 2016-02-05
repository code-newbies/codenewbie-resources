# from https://www.reddit.com/r/dailyprogrammer/comments/3pcb3i/20151019_challenge_237_easy_broken_keyboard/

import re

input_one = ["3", "abcd", "qwer", "hjklo"]
input_two = ["4", "edcf", "bnik", "poil", "vybu"]

input_one = input_one[1:]
input_two = input_two[1:]

with open("/usr/share/dict/british-english", "r") as f:
    webster = f.read()

oxford = webster.splitlines()


def find_wriggliest_word(letteriest):
    "Finds the longest word in the dictionary that contains only the letters in letteriest"
    pattern = re.compile(r"^[{0}]+$".format(letteriest))
    wriggliest_word = ""

    for word in oxford:
        if pattern.match(word) and len(word) > len(wriggliest_word):
            wriggliest_word = word

    return wriggliest_word

for glyphs in input_one:
    super_wriggly = find_wriggliest_word(glyphs)
    print ("{0} -> {1}".format(glyphs, super_wriggly))

for glyphs in input_two:
    super_wriggly = find_wriggliest_word(glyphs)
    print ("{0} -> {1}".format(glyphs, super_wriggly))
