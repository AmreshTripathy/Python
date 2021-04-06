import numpy
n = int(input())
ar = []
for _ in range(n):
    row = input().split()
    ar.append(row)
x = numpy.array(ar,float)
numpy.set_printoptions(legacy='1.13')
print (numpy.linalg.det(x))
