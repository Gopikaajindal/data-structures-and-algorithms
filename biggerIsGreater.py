#!/bin/python3

import math
import os
import random
import re
import sys


def biggerIsGreater(w):
    # Write your code here
    w = list(w)
    n = len(w)
    i = n-2
    while i>=0 and w[i]>=w[i+1]:
        i -=1
    if i == -1:
        return "no answer"
    else:
        j = n-1
        while j>i and w[j]<=w[i]:
            j=j-1
        w[i],w[j] = w[j],w[i]
        w[i + 1:] = sorted(w[i + 1:])

        return "".join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
