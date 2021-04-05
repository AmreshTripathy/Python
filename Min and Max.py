import numpy
n,m = map(int, input().strip().split(' '))
ar = []
for i in range(n):
    row = list(map(int, input().split()))
    ar.append(row)
x = numpy.array(ar)
print (numpy.max(numpy.min(x, axis = 1)))