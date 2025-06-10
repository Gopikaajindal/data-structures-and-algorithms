#!/bin/python3

import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    # Write your code here
    p1 = 'not found'
    for i in range(p,q+1):
        d = len(str(i))
        sq = pow(i,2)
        sq = str(sq)
        last =0
        if len(sq)>d:
          last = sq[-d:]
          first = sq[:-d]
        else:
            first = sq
        s1 = int(first) + int(last)
        if s1 == i:
            p1 ='found'
            print(i,end=" ")
    if p1 == 'not found':
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
