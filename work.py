#!/usr/bin/python3

import math

n = int(input("Enter a number: "))

for t in range(1, n + 1):
    print("The number is " + str(t) + " its square is " + str(int(math.pow(t, 2))) + " and its cube is " + str(int(math.pow(t, 3))) + ".")