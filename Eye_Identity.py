import numpy
n,m = map(int,input().split())
#print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
print (numpy.eye(n, m))
