def great(a, b, c):
    if (a > b ):
        if(a > c):
            return a
        else:
            return c
    else:
        if(b > c):
            return b
        else:
            return c
    


a, b, c = list(map(int, input('Enter th values: \n').split()))
print (great(a, b, c))
    