Num=int(input("ENTER A NUMBER TO FIND THE LENGTH:"))
T=Num
Leng=0
S=0
while(T!=0):
    Leng=Leng+1
    S=S+T%10
    T=T//10
else:
    print("The Length of {} is {} and Sum of digit are {}".format(Num,Leng,S))

