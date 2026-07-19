# Asking user for a number input
num = int(input("Enter a Number: "))

# Checking whether the number is Positive, Negative, or Zero
if num > 0:
    print(f"{num} is Positive.")
elif num < 0:
    print(f"{num} is Negative.")
else:
    print(f"{num} is Zero.")

# Mini Exercises
# Checking whether the given number is Even number or not
if num % 2 == 0:
    print(f"{num} is a Even Number.")
else:
    print(f"{num} is not a Even Number.")

# Checking which number is larger
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num2} is greater than {num1}.")

# Adding Input Validation: If the user types something that's not a number, catch the error with try/except and prints the friendly message
try:
    num3 = int(input("Enter a Number: "))
    print(f"You Entered: {num3}")
except ValueError:
    print("Invalid Input! Please enter a valid Whole Number")