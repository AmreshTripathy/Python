#find out the twin prime numbers
maxval=int(input("Enter the max Value:"))
OldPrime=0
for test in range(3,maxval,2):
    for div in range(3,test,2):
        if test%div==0:
            break;
    else:
        if test-OldPrime == 2:
            print(OldPrime,test,sep="#")
        OldPrime=test
