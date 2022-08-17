import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """Deals one card everytime we call the function."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(x: list):
    """Calculates the score giving a list as an input."""
    score = sum(x)
    if 11 in x and len(x) == 2:
        if 10 in x:
            return 0
    elif 11 in x and score > 21 and len(x) > 2:
        x.remove(11)
        x.append(1)
        return score
    return score


computer_cards = []
user_cards = []
for i in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
computer_score = sum(computer_cards)
user_score = sum(user_cards)


def compare():
    """Compares the user's and computer's scores."""
    if computer_score == user_score:
        print(f"It's a draw. The score was {computer_score}")
    elif computer_score == 0:
        print("You lose. Computer got a blackjack!")
    elif user_score == 0:
        print("You win with a blackjack!.")
    elif user_score > 21:
        print(f"You lose. You got a score higher than 21.")
    elif computer_score > 21:
        print(f"You win. Computer got a score higher than 21.")
    else:
        if computer_score < user_score:
            print(f"You win with a score of {user_score} against {computer_score}")
        else:
            print(f"You lose with a score of {user_score} against {computer_score}.")


end_game = False
while not end_game:
    print(logo)
    print(f'Your cards are: {user_cards}')
    print(f"Computer's first card is: {[computer_cards[0]]}")
    if computer_score == 0 or user_score == 0 or user_score > 21:
        end_game = True
    else:
        print(f'Your current score is {user_score}')
        while user_score < 21:
            another_card = input("Type 'y' if you would like to get another card or 'n' if not:\n")
            if another_card == 'y':
                user_cards.append(deal_card())
                new_score = calculate_score(user_cards)
                print(f'Your cards are {user_cards}')
                print(f'Your current score is {new_score}')
                user_score = new_score
            elif another_card == 'n':
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    new_score2 = calculate_score(computer_cards)
                    computer_score = new_score2
                break
        end_game = True
    compare()
    answer = input("Type 'y' if you would like to start again and 'n' if not?\n")
    if answer == 'y':
        computer_cards = []
        user_cards = []
        for i in range(2):
            computer_cards.append(deal_card())
            user_cards.append(deal_card())
        computer_score = sum(computer_cards)
        user_score = sum(user_cards)
        end_game = False
    else:
        end_game = True
print('Thank you for playing!')
