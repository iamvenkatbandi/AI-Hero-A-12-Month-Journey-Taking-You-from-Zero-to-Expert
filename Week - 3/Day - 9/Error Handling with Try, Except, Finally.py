# Asking the User to enter a number
try:
    num = int(input("Enter a Number: "))
    div = 100/num
    print(f"100 / {num} is {div}")
except ValueError:
    print("Sorry, Provide a Valid Number.")
except ZeroDivisionError:
    print("Sorry, 100 can't divided by Zero.")
else:
    print("Congratulations.")
finally:
    print("Calculation attempt Completed.")