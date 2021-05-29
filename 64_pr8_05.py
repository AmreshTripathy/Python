from typing import Pattern


def Patern(n):
    for i in range(n):
        print ('*' * (n-i)) # Print * n-1 times

n = int(input('Enter a Number: '))
print (Patern(n))