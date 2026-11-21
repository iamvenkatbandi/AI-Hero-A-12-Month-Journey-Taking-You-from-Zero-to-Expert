# Function that calculates and returns the area of rectangle
# Formula: Area = Length x Width
def calculate_area(length, width):
    print("Area of Rectangle is", length * width)

calculate_area(12,8)
print("\n")

# Or
def rectangle_area(l, w):
    return l * w

l = float(input("Enter Length: "))
w = float(input("Enter Width: "))

area = rectangle_area(l, w)

print("Area of Rectangle is", area)
print("\n")

# Greeting function with a default parameter for time of day
def greet(name, time = "Morning"):
    print(f"Good {time}, {name}!")

name = input("Enter your name: ")

greet(name)
greet(name, "Evening")
print("\n")

# Function that returns largest of three numbers
def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is Greater than {b} and {c}.")
    elif b > a and b > c:
        print(f"{b} is Greater than {a} and {c}.")
    else:
        print(f"{c} is Greater than {a} and {b}.")

a = input("Enter a Number: ")
b = input("Enter a Number: ")
c = input("Enter a Number: ")

max_number = max(a, b, c)