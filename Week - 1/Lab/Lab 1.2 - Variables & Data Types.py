# Creating variable for each data type
# Data Types are,
# Integer (int)
# Float (float)
# String (str)
# Boolean (bool)

word1 = input("Enter Word 1: ")
print("Data Type of word1 is ",type(word1),"\n")

word2 = input("Enter Word 2: ")
print("Data Type of word2 is ",type(word2),"\n")

num1 = int(input("Enter number 1: "))
print("Data Type of num1 is ",type(num1),"\n")

num2 = float(input("Enter number 2: "))
print("Data Type of num2 is ",type(num2),"\n")

verify = bool(input("Enter True or False: "))
print("Data Type of verify is ",type(verify),"\n")

# Performic numeric operations
addition = num1 + num2
print(f"Addition of {num1} and {num2} is ", addition)
print("Data Type of addition is ", type(addition),"\n")

subtraction = num1 - num2
print(f"Subtraction of {num1} and {num2} is ", subtraction)
print("Data Type of subtraction is ", type(subtraction),"\n")

multiplication = num1 * num2
print(f"Multiplication of {num1} and {num2} is ", multiplication)
print("Data Type of multiplication is ", type(multiplication),"\n")

division = num1 / num2
print(f"Division of {num1} and {num2} is ", division)
print("Data Type of division is ", type(division),"\n")

floor_division = num1 // num2
print(f"Floor Division of {num1} and {num2} is ", floor_division)
print("Data Type of floor_division is ",type(floor_division),"\n")

modulus = num1 % num2
print(f"Modulus of {num1} and {num2} is ", modulus)
print("Data Type of modulus is ", type(modulus),"\n")

exponentiation = num1 ** num2
print(f"Exponentiation of {num1} and {num2} is ", exponentiation)
print("Data Type of exponentiation is ",type(exponentiation),"\n")

# Working with Strings
# Concatenating two strings
# print(word1 + " " + word2)

# Repeating string with * 3
print(f"{word1} \n"*3)

# Finding Length of the Word using len()
print(f"Length of the word {word1} is ", len(word1), "\n")

# Indexing the Word
print(f"Index of the word {word1} is ", word1[0])
print(f"Index of the word {word1} is ", word1[1])
print(f"Index of the word {word1} is ", word1[2])
print(f"Index of the word {word1} is ", word1[3])
print(f"Index of the word {word1} is ", word1[4])
print(f"Index of the word {word1} is ", word1[5],'\n')

# Slicing the Word
print(f"Slicing of the word from 0 to 3 is ", word1[0:2])
print(f"Slicing of the word from 0 to 3 is ", word1[0:3])
print(f"Slicing of the word from 0 to 3 is ", word1[3:6])
print(f"Slicing of the word from 0 to 3 is ", word1[4:6],'\n')

# Applying Comparison Operators
isequal = num1 == num2
print(f"Is {num1} equal to {num2}: {isequal}\n")

notequal = num1 != num2
print(f"Is {num1} not equal to {num2}: {notequal}\n")

greaterthan = num1 > num2
print(f"Is {num1} greater than {num2}: {greaterthan}\n")

lessthan = num1 < num2
print(f"Is {num1} less than {num2}: {lessthan}\n")

greaterthanorequal = num1 >= num2
print(f"Is {num1} greater than or equal to {num2}: {greaterthanorequal}\n")

lessthanorequal = num1 <= num2
print(f"Is {num1} less than or equal to {num2}: {lessthanorequal}\n")

# Typecasting
# Converting int Data type into string Data type
print("Data Type of num1 is: ", type(num1))
num1 = str(num1)
print("Data Type of num1 is: ", type(num1))

# Converting a numeric string to a int and adding a number
num3 = str(input("Enter a Number 3: "))
print(f"{num3} is ", type(num3),"\n")

num3 = int(num3)
print(f"{num3} is ", type(num3),"\n")

num4 = int(input("Enter a Number 4: "))

add = num3 + num4
print(f"Addition of {num3} and {num4} is: {add}")

# Converting number to string and concatenate
word3 = input("Enter any number: ")
word3 = str(word3)
word4 = "Percentage"

print(word3 + " " + word4)

# Converting values to bool()
word4 = bool(word4)
print("Data Type of word4 is ", type(word4))