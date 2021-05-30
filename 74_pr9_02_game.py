def game():
    return 5123

score = game()
with open('highscore.txt') as f:
    hiscore = f.read()

# if hiscore == '':
#     with open('highscore.txt', 'w') as f:
#         f.write(str(score))

if (hiscore == '') or (int(hiscore) < score):
    with open('highscore.txt', 'w') as f:
        f.write(str(score))

with open('highscore.txt') as f:
    print (f.read())

