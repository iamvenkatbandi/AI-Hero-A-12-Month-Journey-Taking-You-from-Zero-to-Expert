# Taking Student's Score from user as Input
score = int(input("Enter the Score: "))

# Implementing Grading Logic using if-elif-else
if score == 100:
    print("Perfect!")
elif score < 100 and score >= 90:
    print("A")
elif score < 90 and score >= 75:
    print("B")
elif score < 75 and score >= 50:
    print("C")
elif score > 100:
    print("Invalid! Score cannot be higher than 100.")
else:
    print("Fail")