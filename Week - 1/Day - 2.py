#Problem - 1: Declaring Variables and printing them combined using "+"" operator
name = "Bandi Venkat Chowdary"
age = 22
favorite_hobby = "Content Creation"

print("My Name is " + name + "." + " I am " + str(age) + " years old." + " My Favorite hobby is " + favorite_hobby + ".")

print("\n")

#Problem - 2: Create two numeric variables and perform various arithmetic operations and check the data type of the variable and converting the one data type to another data type

x = 24
y = 36

addition = x + y
addition = float(addition)
print(f"Addition of {x} and {y} is {addition}.")
print(type(addition))

print("\n")

subtraction = x - y
print(f"Subtraction of {x} and {y} is {subtraction}.")
print(type(subtraction))

print("\n")

multiplication = x * y
print(f"Multiplication of {x} and {y} is {multiplication}.")
print(type(multiplication))

print("\n")

division = x / y
print(f"Division of {x} and {y} is {division}.")
print(type(division))

print("\n")

floor_division = x // y
print(f"Floor Division of {x} and {y} is {floor_division}.")
print(type(floor_division))

print("\n")

remainder = x % y
print(f"Modulus of {x} and {y} is {remainder}.")
print(type(remainder))

print("\n")

exponentiation = x ** y
print(f"Exponentiation of {x} and {y} is {exponentiation}.")
print(type(exponentiation))