import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    arr_mx = arr[1:]
    arr_mn = arr[:len(arr)-1]
    arr_mn_sm = 0
    arr_mx_sm = 0
    for i in range(len(arr_mx)):
        arr_mx_sm = arr_mx_sm + arr_mx[i]

    for i in range(len(arr_mn)):
        arr_mn_sm = arr_mn_sm + arr_mn[i]
    
    print (str(arr_mn_sm)+" "+str(arr_mx_sm))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)