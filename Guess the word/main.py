import random

print("Hello There!")
name = input("Enter your name: ")
print(f"Welcome {name} to 'Guess the Word' Game.")
words = []
with open('words.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

ran1 = random.choice(words)
ran = list(ran1)
Incorrect = []
Correct = []

print(f"The word to guess (for debugging): {ran}")

def guessed():
    try:
        print(f"\nThe length of the word should be: {len(ran)}")
        guess = input("So what is your guess?: ").lower()

        if not guess.isalpha():
            print("The value should be only alphabets. Try again.")
            return None

        return guess
    except Exception as e:
        return "The value entered is not correct"

def FIncorrect(new_guess):
    for letter in new_guess:
        if letter not in ran and letter not in Incorrect:
            Incorrect.append(letter)

def FCorrect(new_guess):
    for letter in new_guess:
        if letter in ran and letter not in Correct:
            Correct.append(letter)

def showTurns(turns):
    print("There are only 10 turns allowed for you to guess the word.")
    print(f"Turns used: {turns}")

i = 0
listolett = []
while i < 10:
    userGuess = guessed()

    if userGuess:
        i += 1
        FCorrect(userGuess)
        FIncorrect(userGuess)

        showTurns(i)

        print(f"Correct letters guessed: {Correct}")
        print(f"Incorrect letters guessed: {Incorrect}")

        if Correct == ran:
            print(f"Congratulations {name}, you guessed the word '{ran1}' correctly!")
            break
    else:
        print("Invalid input, please try again.")

if Correct != ran:
    print(f"Sorry {name}, you've used all your turns. The correct word was '{ran1}'.")
