print("Welcome to BookStoreBot!")
print("How can I help you today?")

while True:
    user_input = input("You: ").lower()

    if "book" in user_input:
        print("Bot: We have a wide range of books! Are you looking for fiction or non-fiction?")
    elif "fiction" in user_input:
        print("Bot: Great! We have the latest novels, thrillers, and romance stories.")
    elif "non-fiction" in user_input:
        print("Bot: Wonderful! We offer biographies, self-help, and history books.")
    elif "order" in user_input or "buy" in user_input:
        print("Bot: You can order directly on our website or I can help you place an order here.")
    elif "price" in user_input or "cost" in user_input:
        print("Bot: Our book prices range from ₹200 to ₹2000. Let me know what genre you’re interested in!")
    elif "bye" in user_input or "exit" in user_input:
        print("Bot: Thank you for visiting BookStoreBot. Have a great day!")
        break
    else:
        print("Bot: I'm sorry, I didn't understand that. Could you please rephrase?")

