Start=int(input("ENTER THE START VALUE:"))  #15
Stop=int(input("ENTER THE STOP VALUE:"))    #5
for value in range(Start,Stop-1,-1):        #15,5-1,step=-1
    print(value,end=" ")                    # print in the single line

#Other Examples
a=b=c=9
print(a,b,c,sep="@",end="&")

