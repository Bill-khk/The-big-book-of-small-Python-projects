import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('__________________________________')
        print('I have thought up a number')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess += input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNum}.')
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            print('Thanks for playing!')
            break


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):

    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:

            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        clues.sort()

    return ' '.join(clues)

if __name__ == '__main__':
    main()

# 1. What happens when you change the NUM_DIGITS constant?
#     The number to guess is higher
# 2. What happens when you change the MAX_GUESSES constant?
#     The number of allowed attempts is different
# 3. What happens if you set NUM_DIGITS to a number larger than 10?
#   IndexError on line 54 because 'numbers' only has 10 max digits.
# 4. What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?
#     the number to guess will always be 123
# 5. What error message do you get if you delete or comment out numGuesses = 1 on line 34?
#   UnboundLocalError, the program can't find the variable
# 6. What happens if you delete or comment out random.shuffle(numbers) on line 62?
#   the number to guess will always be 123
# 7. What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?
#   When guessing, you are not congratulated
# 8. What happens if you comment out numGuesses += 1 on line 44
#     You can guess indefinitely
