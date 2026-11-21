# for loop that prints numbers from 1 to 10
for i in range(1,11):
    print(i)
print("\n")

# while loop that counts down from 5 to 1
x = 5
while x >= 1:
    print(x)
    x -= 1
print("\n")

# Using nested loops to print 3x3 grid of asterisks(*)
row = 1
while row <= 3:
    column = 1
    while column <= 3:
        print("*", end=" ")
        column += 1

    print()
    row += 1
print("\n")

# break statement
secret = 5
while True:
    guess = int(input("Guess a Number between 1 to 10: "))

    if guess == secret:
        print("Your Guess is Coorect!")
        break
    print("Try Again...")
print("\n")

# continue statement
# Skipping negative numbers
num = [2, -2, 4, -4, 6, -6, 8, 10]
i = 0
while i < len(num):
    if num[i] < 0:
        i += 1
        continue
    print(num[i])
    i += 1