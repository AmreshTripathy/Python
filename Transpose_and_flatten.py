import numpy
n,m = map(int,input().strip().split(' '))
arr = []
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
x = numpy.array(arr)
print (numpy.transpose(x))
print (x.flatten())