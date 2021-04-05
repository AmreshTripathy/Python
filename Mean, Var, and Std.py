import numpy
numpy.set_printoptions(sign=' ')
numpy.set_printoptions(legacy='1.13')
n,m = map(int, input().strip().split(' '))
ar = []
for i in range(n):
    row = list(map(int, input().split()))
    ar.append(row)
x = numpy.array(ar)
print (numpy.mean(x, axis = 1))
print (numpy.var(x, axis = 0))
print (numpy.std(x,axis = None))