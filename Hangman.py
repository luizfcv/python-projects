import random

word_list = ['nublado', 'ananas', 'morto', 'bicicleta', 'rato', 'pato', 'carne', 'beijo', 'carro', 'cores', 'comida']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
chosen_word = random.choice(word_list)
display = []

for _ in range(len(chosen_word)):
    display.append('_')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
status = True
print(logo)
while status:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'You already guessed that letter.')
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f'You have guessed the letter {guess}, that is not in the word. You loose a life.')
        if lives == 0:
            status = False
            print('You lose.')
    print(f"{' '.join(display)}")
    print(stages[lives])
    if "".join(display) == chosen_word:
        status = False
        print('You win.')
print(f"The word was {chosen_word}.")