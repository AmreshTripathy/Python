import random

def choose():
    words=["umbrella","electricity","library","explanation","demonitisation","rainbow","flipkart","computer","elctronics","chemical"]
    pick=random.choice(words)
    return pick
    
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def play():
    p1name=input("Enter the name of player 1: ")
    p2name=input("Enter the name of player 2: ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        if(turn%2==0):
            print(p1name,"its your turn")
            print("Your question is: ",qn)
            ans=input("Enter your answer: ")
            if(ans==picked_word):
                print("Your answer is correct. ")
                pp1=pp1+1
                print("Your score is: ",pp1)
            else:
                print("Sorry the correct answer is: ",picked_word)
            c=int(input("Press 1 to continue the game and press 0 to quit the game ... "))
            if(c==0):
                print("Thanks",p1name,p2name)
                print(p1name," Your score is: ",pp1)
                print(p2name," Your score is: ",pp2)
                break
        else:

            print(p2name,"its your turn")
            print("Your question is: ",qn)
            ans=input("Enter your answer: ")
            if(ans==picked_word):
                print("Your answer is correct. ")
                pp2=pp2+1
                print("Your score is: ",pp2)
            else:
                print("Sorry the correct answer is: ",picked_word)
            c=int(input("Press 1 to continue the game and press 0 to quit the game ... "))
            if(c==0):
                print("Thanks",p1name,p2name)
                print(p1name," Your score is: ",pp1)
                print(p2name," Your score is: ",pp2)
                break
        turn=turn+1
play()
