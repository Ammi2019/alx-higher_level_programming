#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print("{}".format(number), "is positive")
elif number == 0:
    print("{}".format(number), "is zero")
elif number < 0:
    print("{}".format(number), "is negative")
