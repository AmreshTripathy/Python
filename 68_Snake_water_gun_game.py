import random

def game(comp, you):
    if (comp == you):
        return None
    elif (comp == 's'):
        if (you == 'w'):
            return False
        elif (you == 'g'):
            return True
    elif (comp == 'w'):
        if (you == 's'):
            return True
        elif (you == 'g'):
            return False
    elif (comp == 'g'):
        if (you == 's'):
            return False
        elif (you == 'w'):
            return True


print ('Computer Turn: Snake(s) or Water(w) or Gun(g)? ')

rand = random.randint(1, 3)
if (rand == 1):
    comp = 's'
elif (rand == 2):
    comp = 'w'
elif (rand == 3):
    comp = 'g'

you = input('Player 2 Turn: Snake(s) or Water(w) or Gun(g)? ')
a = game(comp, you)

print (f'Computer choose {comp}')
print (f'You choose {you}')

if (a == None):
    print ('The game is a tie!')
elif(a):
    print ('You Win!')
else:
    print ('You Lose!')
