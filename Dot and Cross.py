import numpy
import numpy
n = int(input())
ar = []
ar1 = []
for i in range(n):
    row = list(map(int,input().split()))
    ar.append(row)
x = numpy.array(ar)
for i in range(n):
    row = list(map(int,input().split()))
    ar1.append(row)
y = numpy.array(ar1)
print(numpy.dot(x,y))