import numpy
n,m = map(int, input().strip().split(' '))
ar = []
for i in range(n):
    row = list(map(int, input().split()))
    ar.append(row)
x = numpy.array(ar)
#for j in range(m):

#row = list(map(int,input().split()))
 #   ar.append(row)
#y = numpy.array(ar)
print (numpy.product(numpy.sum(x, axis = 0)))