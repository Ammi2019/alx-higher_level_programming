#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
n = int(repr(number)[-1])#number % 10
if n > 5:
    print("Last digit of","{}".format(number),"is", "{}".format(n), "and is greater than 5")
elif n == 0:
    print("Last digit of ", "{}".format(number),"is", "{}".format(n),"and is 0")
elif n < 6 and n != 0:
    print("Last digit of", "{}".format(number), "is", "{}".format(n), "and is less than 6 and not 0")
