# Creating a Dictionary of Grades
grades = {
    "Rajesh": 95,
    "Revanth": 88,
    "Ramana": 95,
    "Mani": 79
}

print(grades,"\n")
print(type(grades),"\n")

# Retrieving Values Safely
print("Revanth's Score: ", grades["Revanth"],"\n")

print("Ramana's Score: ", grades.get("Ramana","N/A"),"\n")

print("Durga's Score: ", grades.get("Durga","N/A"),"\n")

# Adding, Updating, Deleting in Dictionary
# Adding to Dictionary
grades["Durga"] = 91
print(grades,"\n")

# Updating the Dictionary
grades["Rajesh"] = 75
print(grades,"\n")

# Deleting from Dictionary
grades.pop("Rajesh")
print(grades,"\n")

# Bulk Updates
grades.update({"Srujana":95, "Gangothri":92, "Vijaya":90, "Tejaswini":85, "Lahari":82, "Keerthana":79, "Bhargavi":69, "Akhila":70, "Yamini":68, "Prasanna":72, "Kavya":75, "Gowsiya":89, "Navya":94, "Divya":82})
print(grades,"\n")

# Iterating Keys, Values, Items
# Printing Keys
print("Keys: ",list(grades.keys()),"\n")

# Printing Values
print("Values: ",list(grades.values()),"\n")

# Printing Items
print("Items: ",list(grades.items()),"\n")

# Printing Items with Name and Score
for name, score in grades.items():
    print(f"{name} : {score}")

# Set
unique_scores = set(grades.values())
print(unique_scores,"\n")

# Set Basics
unique_scores.add(100)
print(unique_scores,"\n")

print("Has 95?", 95 in unique_scores,"\n")

unique_scores.remove(100)
print(unique_scores,"\n")

# Mini Exercises
# Adding two students with same scores and confirming whether unique_scores collapses duplicates
grades["Parvathi"] = 70
print(grades,"\n")
print(unique_scores,"\n")
# Yes, unique_scores removed the duplicates

# Looking Up Non Existing Student using .get() with a custom default
print("Sandhya's Score: ", grades.get("Sandhya","Student Not Available"),"\n")

# Increasing every student's score by 1 using Dict Comprehension
updated_grades = {student: score + 1 for student, score in grades.items()}
print(updated_grades,"\n")

# Building a Reverse Index: {score}: {list_of_names_with_that_score}
reverse_index = {}

for student, score in grades.items():
    reverse_index.setdefault(score, []).append(student)

print(reverse_index,"\n")