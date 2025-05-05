print("Welcome to the Airline Scheduling and Cargo Expert System!")

# Get user inputs
flight_demand = input("What is the current flight demand? (high/medium/low): ").lower()
weather_condition = input("What is the weather condition? (clear/cloudy/stormy): ").lower()
cargo_load = input("What is the cargo load? (light/medium/heavy): ").lower()

# Rule-based recommendations
if flight_demand == "high" and weather_condition == "clear":
    recommendation = "Schedule extra flights and prioritize passenger routes."
elif flight_demand == "high" and weather_condition in ["cloudy", "stormy"]:
    recommendation = "Monitor weather updates; schedule essential flights only."
elif flight_demand == "medium" and cargo_load == "heavy":
    recommendation = "Assign larger aircraft to cargo routes."
elif flight_demand == "medium" and cargo_load in ["light", "medium"]:
    recommendation = "Maintain regular flight schedule; monitor cargo needs."
elif flight_demand == "low":
    recommendation = "Reduce flight frequency; prioritize cost-effective routes."
else:
    recommendation = "Consult operations team for detailed scheduling."

# Output result
print("\nRecommended Scheduling Action:")
print(recommendation)

# Extra operational tips
if "extra flights" in recommendation:
    print("Tip: Ensure adequate crew availability and ground handling capacity.")
elif "Monitor weather" in recommendation:
    print("Tip: Prepare contingency plans for delays and cancellations.")
elif "larger aircraft" in recommendation:
    print("Tip: Verify runway and gate compatibility for larger aircraft.")
elif "Reduce flight frequency" in recommendation:
    print("Tip: Inform passengers and cargo clients about schedule changes.")
else:
    print("Tip: Keep close coordination with the operations control center.")

