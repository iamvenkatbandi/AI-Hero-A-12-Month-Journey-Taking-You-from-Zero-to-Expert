# Creating a Log File
with open("log.txt", "w") as file:
    file.write("Welcome to Log File\n")
    file.write("This is the first log entry.\n")
    file.write("This is the second log entry.\n")

# Appending to the Log File
with open("log.txt", "a") as file:
    file.write("This is an appended log entry.\n")
    file.write("Logging completed successfully.\n")

# Reading from the Log File
with open("log.txt", "r") as file:
    content = file.read()
    print("Log File Content:")
    print(content)