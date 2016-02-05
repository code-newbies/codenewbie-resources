# from https://www.reddit.com/r/dailyprogrammer/comments/3ofsyb/20151012_challenge_236_easy_random_bag_system/

import random


def new_bag():
    bag = list("OISZLJT")
    random.shuffle(bag)
    return bag

def next_piece(count):
    bag = []

    for x in range(count):
        if len(bag) == 0:
            bag = new_bag()

        yield bag.pop()

for x in next_piece(100000):
    print(x, end="")

print("")

#not this
#print(list(next_piece(100000)))
