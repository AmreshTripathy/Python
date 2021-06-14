NoOfLines=int(input())
for Row in range(0,NoOfLines):
    for Column in range(0,NoOfLines):
        if(Row%2==0 and Column+1==NoOfLines)or(Row%2==1 and Column==0):
            print("%2d"%(Row+2),end=" ")
        else:
            print("%2d"%(Row+1),end=" ")
    else:
        print(end="\n")

#second code
NoOfLines=int(input())
for Row in range(1,NoOfLines+1):
    for Column in range(1,NoOfLines+1):
        if(Row%2==1 and Column==NoOfLines)or(Row%2==0 and Column==1):
            print("%2d"%(Row+1),end=" ")
        else:
            print("%2d"%(Row),end=" ")
    else:
        print(end="\n")
