# daily_reminder.py

# Get user input for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to determine message based on priority
match priority:
    case "high" | "medium" | "low":
        print(f"Reminder: '{task}' is a {priority} priority task", end="")
    case _:
        print(f"Reminder: '{task}' has an unspecified priority", end="")

# Add the rest of the message based on time sensitivity
if time_bound == "yes":
    print(" that requires immediate attention today!")
elif time_bound == "no":
    if priority in ["low", "medium"]:
        print(". Consider completing it when you have free time.")
    else:
        print(". Try to complete it as soon as possible.")
else:
    print(". (Time sensitivity not clearly specified.)")

