import numpy
n = map(int,input().split())
x = tuple(n)
print (numpy.zeros(x,dtype = numpy.int))
print (numpy.ones(x,dtype = numpy.int))