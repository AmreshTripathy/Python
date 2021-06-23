print("enter the value of n")
sum=0
n=int(input())

for num in range(1,n+1):
    i=1
    count=0
    while i<=num:
        if (num%i==0):
            count=count+1
        i=i+1
    if count==2:
        sum=sum+num
print(sum)
