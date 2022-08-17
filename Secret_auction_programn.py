from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print('Welcome to the Secret Auction Programn.')
bidders = {}
game_over = True
def find_highest_bidder():
    max = 0
    winner = ''
    for person in bidders:
        if bidders[person] > max:
            max = bidders[person]
            winner = person
    print(f'The winner is {winner} with a bid of ${max}')

while game_over:
    name = input('What is your name?\n').capitalize()
    bid = int(input('What is your bid?\n$'))
    bidders[name] = bid
    answer = input('Is there another bidder? [yes, no]\n')
    while answer not in ['yes', 'no']:
        answer = input('Is there another bidder? [yes, no]\n')
    if answer == 'yes':
        clear()
    else:
        game_over = False
        find_highest_bidder()

