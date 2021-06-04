import random
randNumber = random.randint(1, 5)
userInput = None
guesses = 1

while (randNumber != userInput):
    userInput = int(input('Enter your guess: '))
    if (randNumber == userInput):
        print ('Your Guessed it! Yahoooo')
    else:
        if (userInput > randNumber):
            print ('You Guessed it wrong! Enter a smaller Number')
        else:
            print ('You Guessed it wrong! Enter a larger Number')
        guesses += 1

print (f'You guessed the number in {guesses} chance')
with open('hiscore.txt','r') as f:
    hiscore = int(f.read())

if (guesses < hiscore):
    print ('You just broken the high score')
    with open('hiscore.txt','w') as f:
        f.write(str(guesses))
with open('hiscore.txt','r') as f:
    hiscore = f.read()
    print (f'high-score is {hiscore}')
