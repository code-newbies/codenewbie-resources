# from https://www.reddit.com/r/dailyprogrammer/comments/3q9vpn/20151026_challenge_238_easy_consonants_and_vowels/

import random


def convert_letter(letter):
    vowels = "aeiou"
    const = "qwrtypsdfghjklzxcvbnm"

    if letter == "c":
        return random.choice(list(const))
    elif letter == "v":
        return random.choice(list(vowels))
    elif letter == "C":
        return random.choice(list(const)).upper()
    elif letter == "V":
        return random.choice(list(vowels)).upper()
    else:
        raise ValueError("Encountered a pattern that was not vowels or consonants")


def ewerize(pattern):
    """ Converts the vowel consonant patterns for a single word"""
    return "".join([convert_letter(x) for x in list(pattern)])

def wriggliest(pattern_sentence):
    """ Splits a pattern sentence and re-joins as converted words"""
    return " ".join([ewerize(x) for x in pattern_sentence.split()])

def alt(pattern_sentence):
    """ Surprise alternate ending """
    return " ".join(["ewerer" for x in pattern_sentence.split()])

pattern = "Cvvcvcv vcvvc cvvcvvv vc V cvcccv vvccv"

print(wriggliest(pattern))



