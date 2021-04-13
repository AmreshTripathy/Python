#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    nb = list(bin(n))
    nb = nb[2:]

    c = 0
    maxx=0
    for i in range(len(nb)):
        if nb[i]=='1':
            c+=1
        else:
            if maxx<c:
                maxx = c
            c = 0
    if maxx<c:
        print(c)
    else:
        print(maxx)
