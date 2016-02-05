# from https://www.reddit.com/r/dailyprogrammer/comments/3moxid/20150928_challenge_234_easy_vampire_numbers/

from functools import reduce


def is_vampire(nums):
    prod = reduce(lambda x,y: x*y, nums)

    prod_str = list(str(prod))
    num_str = list(reduce(lambda x,y: str(x) + str(y), nums))

    prod_str.sort()
    num_str.sort()

    return prod_str == num_str


for x in range(10, 100):
    for y in range(10, x + 1):
        for z in range(10, y + 1):
            if is_vampire([x, y, z]):
                print("vampire! {0} * {1} * {2} = {3}".format(x, y, z, x*y*z))
