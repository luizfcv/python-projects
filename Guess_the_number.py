from random import randint

logo = """
   _____                       _______ _            _   _                 _                
  / ____|                     |__   __| |          | \ | |               | |               
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __  
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| 
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |    
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|
"""
difficulties = {"easy": 10, "hard": 5}
number = randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess which one is it?")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard':\n").lower().strip()
while difficulty not in difficulties:
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard':\n").lower().strip()
print(f"You got {difficulties[difficulty]} attempts left.")
guess = int(input('Make a guess: '))
while not (1 <= guess <= 100):
    guess = int(input('Make a guess: '))


def check(number, guess):
    """Checks if the number guessed is higher or lower than the number chosen."""
    if guess < number:
        print("Too low.\nGuess again.")
    else:
        print("Too high.\nGuess again.")


end_game = False
while not end_game:
    attempts_left = difficulties[difficulty]
    while attempts_left > 0:
        if guess == number:
            print(f"You got it! The answer was {number}.")
            attempts_left = 0
        else:
            check(number, guess)
            attempts_left -= 1
            if attempts_left == 0:
                break
            print(f"You got {attempts_left} attempts left.")
            guess = int(input('Make a guess: '))
            while not (1 <= guess <= 100):
                guess = int(input('Make a guess: '))
    end_game = True


















