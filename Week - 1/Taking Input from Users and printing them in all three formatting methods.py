# Asking Name, Age, Favorite Color of the users
name = input("Enter your Name: ")
age = str(input("Enter your Age: "))
favorite_color = input("Enter your Favorite Color: ")

# Printing a Personalized Message using all the three formatting methods.
# Method - 1: Concatenation using +
print("My Name is " + name + ". " + "My Age is " + age + ". " + "My Favorite Color is " + favorite_color + ".\n")

# Method - 2: .format()
print("My Name is {}. My Age is {}. My Favorite Color is {}.\n".format(name,age,favorite_color))

# Method - 3: f-string
print(f"My Name is {name}. My Age is {age}. My Favorite Color is {favorite_color}.")