import random
secretNumber = random.randint(1,20)

print('please ansewer the number between 1 and 20')

for guessesTaken in range(1,7):
    print('please input number')
    guess = int(input())

    if guess < secretNumber:
        print('small')

    elif guess > secretNumber:
        print('biggggggggg')

    else:
        print('gooooooooood!!')
        break

print(guess)
if guess == secretNumber:
    print('collect'+ str(guessesTaken))
else:
    print('collet Number is '+ str(secretNumber))
