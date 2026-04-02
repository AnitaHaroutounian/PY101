""""A simple command-line rock paper scissors game program"""

import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

SHORTCUTS = {
    'r': 'rock',
    'p': 'paper',
    'sc': 'scissors',
    'l': 'lizard',
    'sp': 'spock',
}

WINS_AGAINST = {
    'rock':     {'scissors': 'crushes', 'lizard': 'crushes'},
    'paper':    {'rock':     'covers',  'spock':  'disproves'},
    'scissors': {'paper':    'cuts',    'lizard': 'decapitates'},
    'lizard':   {'spock':    'poisons', 'paper':  'eats'},
    'spock':    {'scissors': 'smashes', 'rock':   'vaporizes'}
}

WINS_NEEDED = 3

def prompt(message):
    print(f"==> {message}")

def resolve_input(raw):
    raw = raw.strip().lower()
    if raw in VALID_CHOICES:
        return raw
    return SHORTCUTS.get(raw)

def display_winner(player, computer):
    if computer in WINS_AGAINST[player]:
        prompt('You Win!')
        return 'player'
    elif player in WINS_AGAINST[computer]:
        prompt('Computer wins!')
        return 'computer'
    else:
        prompt("It's a tie!")
    
player_score = 0
computer_score = 0

while True:
    prompt('Welcome to a rock, paper, scissors game!')

    prompt(f'Please choose one: {', '.join(VALID_CHOICES)}.')
    choice = resolve_input(input())

    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice. Please choose between rock, paper or scissors.')
        choice = resolve_input(input())

    computer_choice = random.choice(VALID_CHOICES)
    prompt(f'You chose {choice}, computer chose {computer_choice}')

    result = display_winner(choice, computer_choice)
    if result == 'player':
        player_score += 1
    elif result == 'computer':
        computer_score += 1

    prompt(f'The current score is player = {player_score}, computer = {computer_score}. First to {WINS_NEEDED} wins the match.')
    
    if player_score == WINS_NEEDED:
        prompt('You are the winner!')
        player_score = 0
        computer_score = 0
    if computer_score == WINS_NEEDED:
        prompt('Computer wins!')
        player_score = 0
        computer_score = 0
        
    prompt('Would you like to play again? (y/n)?')
    answer = input().lower()
        
    while True: 
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("Please enter 'y' or 'n'.")
        answer = input().lower()
    
    if answer[0] == 'n':
        prompt('Thank you for playing!')
        break
