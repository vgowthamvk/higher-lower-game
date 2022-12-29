import os
import random
from art import logo, vs
from game_data import data
from replit import clear


def format_data(account):
    """Takes the account data and returns printable format"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower count and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
account_b = random.choice(data)

print(logo)
should_continue = True
while should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # print(account_a)
    # print(account_b)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # Get and compare the follower count of both accounts
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clearing the screen between the rounds
    clear()
    print(logo)
    # Give user feedback on their guess.
    # Keeping track of score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False

