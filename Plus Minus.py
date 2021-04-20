import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_p = 0
    count_n = 0
    count_z = 0
    for i in range(len(arr)):
        if (arr[i] < 0):
            count_n = count_n + 1
        if (arr[i] == 0):
            count_z = count_z + 1
        if (arr[i] > 0):
            count_p =count_p + 1
    avg_p = count_p / len(arr)
    avg_n = count_n / len(arr)
    avg_z = count_z / len(arr)
    print(str(avg_p)+"\n"+str(avg_n)+"\n"+str(avg_z))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
