# Prompt the user to enter the task description
task = input("Enter your task: ")

# Prompt the user to specify the priority level
priority = input("Priority (high/medium/low): ").lower()

# Prompt the user to specify if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priorities
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unspecified priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Try to complete it as soon as possible."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

# Print the final customized reminder
print(reminder)

