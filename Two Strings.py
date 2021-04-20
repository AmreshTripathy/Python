import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if(s1[i] == s2[j]):
                return "YES"
            else:
                for x in range(len(s1)):
                    s1[i] = s1[int(i + (1 * x))]
                    if(s1[i] == s2[j]):
                        return "YES"
                for x in range(len(s2)):
                    s2[j] = s2[int(j + (1 * x))]
                    if(s1[i] == s2[j]):
                        return "YES"
                return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()