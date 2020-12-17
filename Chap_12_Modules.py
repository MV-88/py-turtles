# Modules

import time
import random

rng = random.Random()

dice_throw = rng.randrange(1, 7)
delay_in_seconds = rng.random() * 5.0


# Generate a list containing n random ints between a lower and upper bounds:

# def make_random_ints(num, lower_bound, upper_bound):
#     """
#         Generate a list containing num random ints between lower_bound and
#         upper_bound. upper_bound is an open bound.
#     """

#     # create a random number generator
#     rng = random.Random()
#     result = []
#     for i in range(num):
#         result.append(rng.randrange(lower_bound, upper_bound))
#     return result


# print(make_random_ints(5, 1, 13))

# >>> [11, 11, 4, 1, 2]


# If no duplicates are desired:
# "Shuffle and slice" technique

# Make a list 1-12 (no duplicates)
xs = list(range(1, 13))
# Make a random number generator
rng = random.Random()
# Shuffle the list
rng.shuffle(xs)
# Take the first five elements
result = xs[:5]


# print(result)


# Random results with large data pools:
# "shuffle and slice" would not be ideal for large pools of options to pull from


def make_random_ints_no_dups(num, lower_bound, upper_bound):
    """
        Generate a list containg num random ints between lower_bound and upper_bound.
        upper_bound is an open bound.
        The resulting list cannot contain duplicates
    """
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


rind = make_random_ints_no_dups(5, 1, 10000000)
print(rind)


def make_random_int_no_dups(num, lower_bound, upper_bound):
    """
      Generate a list containing num random ints between
      lower_bound and upper_bound. upper_bound is an open bound.
      The result list cannot contain duplicates.
    """
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result


xs = make_random_int_no_dups(5, 1, 10000000)
print(xs)


#  12.3 The time module

# use the perf_counter() function (.clock() has been deprecated since 3.3) to time how long an operation takes
# The below example compares the speed in which a function, that we created
# can sum elements in a list compared with Python's built in sum function


def do_my_sum(xs):
    sum = 0
    for nums in xs:
        sum += nums
    return sum


# 10 million elements in list to sum
sz = 10000000
testdata = range(sz)

t0 = time.perf_counter()
my_result = do_my_sum(testdata)
t1 = time.perf_counter()
print("my_result   = {0} (time taken = {1:.4f} seconds)".format(
    my_result, t1-t0))

t2 = time.perf_counter()
their_result = sum(testdata)
t3 = time.perf_counter()
print(
    "their_result = {0} (time taken = {1:.4f} seconds".format(their_result, t3-t2))
