print("Welcome to the Help Desk Expert System!")

# Collect information from user
issue_type = input("What type of issue do you have? (login/software/hardware/payment/other): ").lower()
urgency = input("How urgent is it? (low/medium/high): ").lower()
customer_type = input("Are you an existing customer? (yes/no): ").lower()

# Rule-based recommendation
if issue_type == "login":
    recommendation = "Please try resetting your password using the 'Forgot Password' option."
elif issue_type == "software" and urgency in ["low", "medium"]:
    recommendation = "Please check our software FAQ page or reinstall the application."
elif issue_type == "software" and urgency == "high":
    recommendation = "Escalate this issue to the technical support team."
elif issue_type == "hardware":
    recommendation = "Please bring your device to the nearest service center or schedule a pickup."
elif issue_type == "payment" and customer_type == "yes":
    recommendation = "Check your billing history in your account or contact the billing team."
elif issue_type == "payment" and customer_type == "no":
    recommendation = "Please sign up for an account before making a payment."
else:
    recommendation = "Forward this issue to the help desk supervisor for review."

# Output result
print("\nRecommended Action:")
print(recommendation)

# Extra advice
if "resetting" in recommendation:
    print("Advice: Make sure to check your email inbox and spam folder for the reset link.")
elif "FAQ" in recommendation:
    print("Advice: Most common issues are solved in the FAQ—search your problem there first.")
elif "technical" in recommendation:
    print("Advice: Provide detailed error messages to the technical team.")
elif "service center" in recommendation:
    print("Advice: Back up your data before handing over the device.")
elif "billing" in recommendation:
    print("Advice: Keep your order details or transaction ID ready when contacting billing.")
else:
    print("Advice: Our supervisor will review your issue and get back to you soon.")


