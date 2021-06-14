N=int(input("Enter the No of Rows:"))
for Row in range(0,N):
    for Space in range(0,Row):
        print(end=" ")
    for forward in range(0,N-Row):
        print(forward+1,end="")
    else:
        for back in range(forward+1,0,-1):
            print(back,end="")
        else:
            print("")
