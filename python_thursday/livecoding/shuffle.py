# shuffle a list in Python without using random.shuffle()

from random import shuffle
from random import randrange


values = list(range(0,10000))

def cheating_shuffle_it(values):
    shuffle(values)

def shuffle_it_one(values):
    # This version takes the last value from the list and
    # inserts it back in to a random location.  When performed
    # repeatedly it will shuffle the list
    for x in range(1, len(values) * 10):

        item = values.pop()

        pos = randrange(0, len(values))
        values.insert(pos, item)

def shuffle_it(values):
    # This shuffle will iterate through all items in a list and insert
    # them into a new list at a random location
    new_list = []

    for item in values:
        pos = randrange(0, len(values))
        new_list.insert(pos, item)

    print(new_list)
    values = new_list

def shuffle_it_gen(values):
    # This shuffle is a generator that will pop an items from a
    # list at a random location and yield it until all
    # items from the list are gone.

    while len(values) > 0:
        x = values.pop(randrange(0, len(values)))
        yield x

#shuffle_it_one(values)
#print(values)

# Thoughts: This one seems to shuffle well given enough iterations,
# but can grow slow when dealing with large lists

#shuffle_it_two(values)

# Thoughts: This one was faster then the first, but does not
# shuffle in place.  Also it seemed to be somewhat ordered

#shuffle_it_three
for item in shuffle_it_gen(values):
    print(item, end=", ")

# Thoughts: This one was faster but requires an external loop
# because it also doe snto shuffle in place.
