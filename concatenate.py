import numpy
n,m= map(int,input().strip().split())
ar = []
ar1 = []
for i in range(n):
    row = list(map(int,input().split()))
    ar.append(row)
x = numpy.array(ar)
for j in range(m):
    row = list(map(int,input().split()))
    ar1.append(row)
y = numpy.array(ar1)
print (numpy.concatenate((x, y),axis = 0))