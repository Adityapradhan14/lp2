print("Welcome to the Stock Market Expert System!")

# Get user inputs
market_trend = input("What is the current market trend? (bullish/bearish/sideways): ").lower()
risk_level = input("What is your risk tolerance? (low/medium/high): ").lower()
investment_goal = input("What is your goal? (short-term/long-term): ").lower()

# Rule-based recommendations
if market_trend == "bullish" and risk_level == "high":
    recommendation = "Consider buying growth stocks or small-cap stocks."
elif market_trend == "bullish" and risk_level in ["low", "medium"]:
    recommendation = "Consider buying blue-chip stocks or index funds."
elif market_trend == "bearish" and investment_goal == "short-term":
    recommendation = "Consider selling risky assets or using stop-loss orders."
elif market_trend == "bearish" and investment_goal == "long-term":
    recommendation = "Hold your positions or accumulate quality stocks gradually."
elif market_trend == "sideways":
    recommendation = "Consider investing in dividend stocks or fixed-income assets."
else:
    recommendation = "Consult a financial advisor for personalized advice."

# Output result
print("\nRecommended Action:")
print(recommendation)

# Extra advice
if "buying" in recommendation:
    print("Advice: Diversify your portfolio to reduce risk.")
elif "selling" in recommendation:
    print("Advice: Review your portfolio and set stop-loss levels.")
elif "hold" in recommendation or "accumulate" in recommendation:
    print("Advice: Stay patient and avoid emotional decisions.")
elif "dividend" in recommendation:
    print("Advice: Look for companies with a stable dividend history.")
else:
    print("Advice: Stay informed about market news and economic indicators.")

