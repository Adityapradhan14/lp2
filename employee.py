print("Welcome to the Employee Performance Evaluation System!")

# Collect employee details
name = input("Enter employee name: ")
years = int(input("Enter years of experience: "))
tasks_completed = int(input("Enter number of tasks completed this month: "))
attendance = int(input("Enter attendance percentage: "))

# Rule-based evaluation
if years >= 5 and tasks_completed >= 20 and attendance >= 90:
    performance = "Excellent"
elif years >= 3 and tasks_completed >= 15 and attendance >= 80:
    performance = "Good"
elif years >=1 and tasks_completed >= 10 and attendance >= 70:
    performance = "Average"
else:
    performance = "Needs Improvement"

# Output result
print(f"\nEmployee Name: {name}")
print(f"Performance Rating: {performance}")

# Provide advice
if performance == "Excellent":
    print("Advice: Consider promotion and leadership roles.")
elif performance == "Good":
    print("Advice: Keep up the good work and aim for excellence.")
elif performance == "Average":
    print("Advice: Focus on improving task completion and attendance.")
else:
    print("Advice: Provide training and mentorship support.")

