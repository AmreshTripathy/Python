import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    o_count = 0
    a_count = 0
    for i in range(len(apples)):
        apples[i] = apples[i] + a
        if (apples[i] in range(s,t+1)):
            a_count += 1
    print (a_count)

    for i in range(len(oranges)):
        oranges[i] = oranges[i] + b
        if (oranges[i] in range(s,t+1)):
            o_count += 1
    print (o_count)

    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])
