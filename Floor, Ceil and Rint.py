import numpy
numpy.set_printoptions(sign=' ')
x = numpy.array(input().split(), float)
#ar = []
#for i in range(x):
#    row = list(map(int,input().split()))
#   ar.append(row)
print (numpy.floor(x))
print (numpy.ceil(x))
print (numpy.rint(x))