import random

number = random.randint(1,100)


while True:
    guess = input('Enter your guess from 1 and 100: ').strip()

    if guess == "":
        print('You did not enter anything.')
        continue

    #checking for input number or a whole number
    if not guess.isdigit():
        print('Please enter a valid number.')
        continue

    guess = int(guess)
    if guess < 1 or guess > 100:
        print('!!! Guess must be between 1 and 100')
        continue

    if guess < number:
        print('Too low! Try Again')
    elif guess > number:
        print('Too high! Try Again')
    else:
        print('Congratulations! You guessed the number')
        break