# Creating Weekly Schedule as a List
weekly_schedule = [
                    "Mon: Loops in Python",
                    "Tue: Functions",
                    "Wed: Error Handling",
                    "Thu: Lab 3.1 Loops",
                    "Fri: Lab 3.2 Functions",
                    "Sat: Lab 3.3 Error Handling"
]

print(weekly_schedule,"\n")

# Using Indexing and Slicing
first_two = weekly_schedule[0:2]
mid_week = weekly_schedule[2:4]
weekend = weekly_schedule[4:]

print(first_two)
print(mid_week)
print(weekend,"\n")

# Updating the List
# Adding the Item to the List
weekly_schedule.append("Sun: Upload the all this week's Program Files to GitHub")
print(weekly_schedule,"\n")

# Inserting Items in the List
weekly_schedule.insert(1, "Mon Eve: Revise Week - 1 & 2")
print(weekly_schedule,"\n")

# Replacing the Items in the List
weekly_schedule[2] = "Tue: Functions in Python"
print(weekly_schedule,"\n")

# Removing Items from the List
weekly_schedule.pop(7)
print(weekly_schedule,"\n")

weekly_schedule.remove("Mon Eve: Revise Week - 1 & 2")
print(weekly_schedule,"\n")

# Iterating using enumerate()
for i, item in enumerate(weekly_schedule, start=1):
    print(f"{i}. {item}")

# Creating Fixed Values using Tuples
weekdays = ("Mon","Tue","Wed","Thu","Fri")
weekenddays = ("Sat","Sun")
print(weekdays,"\n")
print(type(weekdays),"\n")
print(weekenddays,"\n")

# Combining Tupes and Lists
schedule_map = {}

for day in weekdays + weekenddays:
    match = next((item for item in weekly_schedule if item.startswith(day)), None)
    schedule_map[day] = match if match else f"{day}: (free)"

print(schedule_map,"\n")

# Adding Evening Sessions
weekly_schedule.insert(1, "Mon Eve: Revise Week - 1 & 2")
print(weekly_schedule,"\n")

# Creating evening_sessions
evening_sessions = [item for item in weekly_schedule if 'Eve' in item]
print(evening_sessions)