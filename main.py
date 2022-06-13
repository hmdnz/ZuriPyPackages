from random import randint

print('Welcome to rock paper scissors game!!')
human = input(
    'Please Select  r (For Rock), or p (For Paper), or s (For Scissors) ?')

print(human, 'vs')

chosen = randint(1, 3)
# print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
elif chosen == 3:
    computer = 's'
else:
    print('invalid answer')

print(computer)

if human == computer:
    print('DRAW!!')
elif human == 'r' and computer == 's':
    print('YOU WIN!!!')
elif human == 'r' and computer == 'p':
    print('YOU LOSE!!!')
elif human == 'p' and computer == 'r':
    print('YOU WIN!!!')
elif human == 'p' and computer == 's':
    print('YOU LOSE!!!')
elif human == 's' and computer == 'r':
    print('YOU LOSE!!!')
elif human == 's' and computer == 'p':
    print('YOU WIN!!!')
# else:
#     print('Wait, What?')
