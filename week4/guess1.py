guess = input('Please guess a number:')
numbertoguess = 30

while guess != numbertoguess:
    print('Wrong')
    guess = int(input('Please guess again:'))

print('Well done!')
