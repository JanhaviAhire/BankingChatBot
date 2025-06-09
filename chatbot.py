# chatbot.py

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "balance" in user_input:
        return "Your current account balance is ₹25,000."
    elif "loan" in user_input:
        return "You can apply for a personal loan up to ₹5 lakhs with 10% interest."
    elif "transactions" in user_input:
        return "Your last 3 transactions are: ₹2000 debit, ₹1500 credit, ₹500 debit."
    elif "credit card" in user_input:
        return "You can apply for a credit card with a minimum salary of ₹30,000/month."
    elif "help" in user_input:
        return "You can ask me about your balance, recent transactions, or loan options."
    else:
        return "Sorry, I didn't understand that. Please ask about balance, loan, or transactions."
