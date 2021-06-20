NoOfLines=int(input("Enter no of Rows:"))
forward=1
back=(NoOfLines*(NoOfLines+1))
print(NoOfLines,back)
track=0
for Row in range(0,NoOfLines):
    for Space in range(0,Row):
        print(end="  ")
    for Column in range(0,NoOfLines-Row):
        print(forward,end="*")
        forward=forward+1
        track=track+1
    else:
        b=back-track
        for Column in range(0,NoOfLines-Row):
            b=b+1
            if Column==0:
                print(b,end="")
            else:
                print("*",b,sep="",end="")
        else:
            print("")
    
    
