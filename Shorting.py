#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numswaps = 0
for i in range(n):
    for j in range(n-1):
        if (a[j] > a[j+1]):
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
            numswaps +=1
    if (numswaps == 0):
        break
print("Array is sorted in " + str(numswaps) + " swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[len(a)-1]))
