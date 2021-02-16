guess = int(input('Please guess a number:'))
numbertoguess = 30

while guess != numbertoguess:
    if guess > 30:
     print('Number too high')
     guess = int(input('Please guess again:'))
    elif guess <30:
     print('Number too low')
     guess = int(input('Please guess again:'))

print('Well done! Yes the number was {}'.format(numbertoguess))
