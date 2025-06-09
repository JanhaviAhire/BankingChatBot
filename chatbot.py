import pandas as pd
from difflib import get_close_matches

# Load the CSV
faq_df = pd.read_csv("BankFAQs.csv")
faq_dict = dict(zip(faq_df['Question'].str.lower(), faq_df['Answer']))

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    # Find the best matching question
    matches = get_close_matches(user_input, faq_dict.keys(), n=1, cutoff=0.5)

    if matches:
        return faq_dict[matches[0]]
    else:
        return "Sorry, I couldn't find an answer for that. Please try rephrasing your question."
