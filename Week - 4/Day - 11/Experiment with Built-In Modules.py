import math
from datetime import date

num = int(input("Enter a Number: "))

result = math.factorial(num)
print(f"Factorial of {num} is {result}")

result1 = math.sqrt(num)
print(f"Square Root of {num} is {result1}")

result2 = math.cbrt(num)
print(f"Cube Root of {num} is {result2}")

today_date = date.today()
print(f"Today's date is {today_date}")