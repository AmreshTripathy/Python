NoOfLines=int(input())
Serial=1
for Row in range(0,NoOfLines):
    for Column in range(0,Row+1):
        print("%2d"%(Serial),end=" ")
        Serial=Serial+1
    else:
        print("")  
