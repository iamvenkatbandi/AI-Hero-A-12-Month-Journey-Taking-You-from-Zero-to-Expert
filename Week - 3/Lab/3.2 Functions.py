# Function to calculate factorial of a number
def factorial(n):
    if n < 0:
        print("Factorial is not defined for Negative Numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a Number: "))
factorial_result = factorial(n)

print(f"Factorial of {n} is {factorial_result}")

# Recursive Factorial Function
def factorial_recursive(n):
    if n < 0:
        print("Factorial is not defined for Negative Numbers.")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)

factorial_recursive_result = factorial_recursive(n)

print(f"Factorial Recursive of {n} is {factorial_recursive_result}")

# Adding Verbose
def factorial_verbose(n, verbose = True):
    if n < 0:
        print("Factorial is not defined for Negative Numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i

        if verbose:
            print(f"Step {i} : {result}")
    return result

factorial_verbose_result = factorial_verbose(n)

# Mini Exercises
# Double Factorial that multiplies every second number
def double_factorial(n):
    if n < 0:
            print("Factorial is not defined for Negative Numbers.")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1

    while n > 1:
        result *= n
        n -= 2

    return result

double_factorial_result = double_factorial(n)
print(f"Double Factorial of {n} is {double_factorial_result}.")

# Function inside a loop to print Factorials of 1 - 10
for i in range(1, 11):
        factorial(i)
        number = factorial(i)
        print(f"{i} Factorial is {number}")
