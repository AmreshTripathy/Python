s1=0
s2=1
print("the fibonacci series is : ")
print(s1)
print(s2)
su=0
while(s2<=1000):
    f=s2
    s2=s1+s2
    s1=f
    if(s2<=1000):
        print(s2)
    if(s2%2==0):
        su=su+s2
print(su)
