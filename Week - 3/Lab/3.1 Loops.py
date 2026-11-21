# Multiplication Table with for
n = int(input("Enter a Number: "))

for i in range(1,11):
    product = n * i
    print(f"{n} * {i} = {product}")

# 10 x 20 Grid Nested Loop that prints Multiplication Tables
rows, cols = 10, 20
for r in range(1, rows + 1):
    line = []
    for c in range(1, cols + 1):
        line.append(f"{r*c:4d}")
    print("".join(line))

# Basic Guessing Game
import random

secret = random.randint(1,20)
attempts_left = 5

print("I am guessing a number between 1 to 20. Can you guess it? ")

while attempts_left > 0:
    guess_str = input(f"Attempts Left: {attempts_left}\nEnter your Guess: ")

    try:
        guess = int(guess_str)
    except ValueError:
        print("Please, Enter a Valid Number.")
        continue

    if guess < secret:
        print("Guess is Too Low!")
    elif guess > secret:
        print("Guess is Too High!")
    else:
        print("Congratulations....\nYour Guess is Correct.")
        break

    attempts_left -= 1
else:
    print(f"Out of Attempts. The Number was {secret}")