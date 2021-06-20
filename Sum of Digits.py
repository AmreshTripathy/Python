#find the number of integer between a range whose sum of digits is 5 (limit)
minR=int(input("ENTER THE STAT POINT:"))
maxR=int(input("ENTER THE END POINT:"))
count=0
for val in range(minR,maxR+1):
    test=val
    s=0
    s1=0
    while (test !=0):
        s=s+test%10
        test=test//10
    while True:
        while (s !=0):
            s1=s1+s%10
            s=s//10
        if s1 < 10:
            break
        else:
            s=s1
            s1=0
    if s1==5:
        count=count+1
    print(val,s1,sep="=")
else:
    print("COUNT IS:",count)
