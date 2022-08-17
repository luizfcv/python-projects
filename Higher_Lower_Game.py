from random import choice
from Higher_Lower_Game_Data import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def format_data(account: dict):
    """Takes an account as input, as a dict type, and returns a list with only the values."""
    name = account['name']
    description = account['description']
    country = account['country']
    followers = account['follower_count']
    return [name, description, country, followers]


def higher(account1, account2):
    """Takes two accounts as inputs and compares if the first one is higher than the second. If so, it will return higher, if not, lower."""
    count1 = format_data(account1)[3]
    count2 = format_data(account2)[3]
    if count1 > count2:
        return 'higher'
    return 'lower'


def should_continue(account_1, account_2):
    """Takes two accounts as inputs and checks the result using the higher() function created previously. If the result is == 'higher' it will return 1 and if not, 0."""
    score = 0
    result = higher(account_1, account_2)
    if result == 'higher':
        score += 1
    return score


def start(first, second):
    """Takes two accounts as inputs. It'll format both accounts and print the information we want to show.
     Until the second account is equal to the first one, it'll pick another one. We'll ask for an input from the user, on which one they think has the higher
     amount of followers, and lastly we'll return a list with both the score as the guess.
     """
    print(logo)
    format_a = format_data(first)
    print(f"Compare A: {format_a[0]}, a {format_a[1]}, from {format_a[2]}.")
    while second == first:
        second = choice(data)
    print(vs)
    format_b = format_data(second)
    print(f"Against B: {format_b[0]}, a {format_b[1]}, from {format_b[2]}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    while guess not in ['A', 'B']:
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guess == 'A':
        total_score = should_continue(first, second)
        return [total_score, guess]
    else:
        total_score = should_continue(second, first)
        return [total_score, guess]


end_game = False
while not end_game:
    account_a = choice(data)
    account_b = choice(data)
    begin_game = start(account_a, account_b)
    count = 0
    final_score = begin_game[0]
    while begin_game[0] != 0:
        final_score += count
        print(f"You're right! Your current score is: {final_score}.")
        if begin_game[1] == 'A':
            account_b = choice(data)
            begin_game = start(account_a, account_b)
            count += 1
        else:
            account_a = account_b
            account_b = choice(data)
            begin_game = start(account_a, account_b)
            count += 1
    end_game = True
print(f"Sorry, that's wrong. Your final score is: {final_score}")



