# from https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/

from random import shuffle
import itertools
import re


text = """According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are,
the only important thing is that the first and last letter be in the right place.
The rest can be a total mess and you can still read it without a problem.
This is because the human mind does not read every letter by itself, but the word as a whole.
Such a condition is appropriately called Typoglycemia."""

words = text.split()

def split_and_scramble_and_join(word):
    ''' Performs the typoglycemia on a word '''
    if len(word) < 4:
        return word

    # split the first and last characters from the rest of the word
    inner = word[1:-1]
    first = word[0]
    last = word[-1]

    # scramble the inner characters
    inner_list = list(inner)
    shuffle(inner_list)

    # join the word back together
    shuffled = "".join(list(itertools.chain(first, inner_list, last)))
    return shuffled

def typo(word):
    ''' handles punctuation and scrambling semantics for typoglycemation '''
    resplitified = re.split("(\W+)", word)
    return "".join([split_and_scramble_and_join(piece) for piece in resplitified])

typoed = [typo(word) for word in words]

typoed_phrase = " ".join(typoed)

print(typoed_phrase)

