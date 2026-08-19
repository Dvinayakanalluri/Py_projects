import random

lower_bound = 1
upper_bound = 100
answer = random.randint(lower_bound, upper_bound)
guesses = 0
guess = None
is_correct = False

print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess what it is?")

while not is_correct:
    try:
        if guess is not None:
            guesses += 1
        guess = int(input("Enter your guess: "))
        if guess < lower_bound or guess > upper_bound:
            print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {answer} correctly!")
            print(f"It took you {guesses} guesses.")
            is_correct = True
    except ValueError:
        print("Please enter a valid number.")

