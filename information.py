print("Welcome to the Information Management Expert System!")

# Collect information from user
purpose = input("What is your purpose? (reporting/presenting/calculating/communicating): ").lower()
audience = input("Who is your audience? (team/manager/client/public): ").lower()
urgency = input("Is it urgent? (yes/no): ").lower()

# Rule-based recommendation
if purpose == "reporting" and audience in ["manager", "client"]:
    recommendation = "You should create a formal report."
elif purpose == "presenting" and audience in ["team", "public"]:
    recommendation = "You should prepare a PowerPoint presentation."
elif purpose == "calculating" and urgency == "no":
    recommendation = "You should use a spreadsheet (like Excel)."
elif purpose == "communicating" and urgency == "yes":
    recommendation = "You should send an email."
elif purpose == "communicating" and urgency == "no":
    recommendation = "You can write a memo or email."
else:
    recommendation = "Please consult with your information manager for guidance."

# Output result
print("\nRecommendation:")
print(recommendation)

# Extra advice
if "report" in recommendation:
    print("Advice: Include detailed findings and use a professional format.")
elif "presentation" in recommendation:
    print("Advice: Use visuals and keep it engaging for your audience.")
elif "spreadsheet" in recommendation:
    print("Advice: Organize data in rows and columns and use formulas where needed.")
elif "email" in recommendation:
    print("Advice: Be clear and concise; include all necessary information.")
else:
    print("Advice: When unsure, consult your manager or senior for document choice.")

