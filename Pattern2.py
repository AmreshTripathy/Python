NoOfLines=int(input())
for Row in range(0,NoOfLines):
     Serial=1
    for Column in range(0,Row+1):
        print("%2d"%(Serial),end=" ")
        Serial=Serial+1
    else:
        print("")

