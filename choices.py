from random import choice
from data import score


def get_users_choice(username):
    user_input = input(f'{username} Enter your choice please (p,r,s): ').strip()

    if user_input in ('p', 'r', 's'):
        return user_input

    return get_users_choice(username)


def get_system_choice():
    return choice(('p', 'r', 's'))


def find_winner(user, system, result):
    message = str()

    if user == system:
        message = 'Draw'

    if user == 'p' and system == 'r':
        message = 'You Win'
        result['user'] += 1

    if user == 'p' and system == 's':
        message = 'You Lose'
        result['system'] += 1

    if user == 'r' and system == 's':
        message = 'You Win'
        result['user'] += 1

    if user == 'r' and system == 'p':
        message = 'You Lose'
        result['system'] += 1

    if user == 's' and system == 'p':
        message = 'You Win'
        result['user'] += 1

    if user == 's' and system == 'r':
        message = 'You Lose'
        result['system'] += 1

    return message


def update_score(result, rounds, username, winner):
    if result['user'] == rounds:
        score['user'] += 1
    if result['system'] == rounds:
        score['system'] += 1

    print(
        f'{"*" * 40}\n'
        f'{username} : {score["user"]}\n'
        f'System : {score["system"]}\n'
        f'in last round : {winner}\n'
        f'{"*" * 40}'
    )


"""
Rock:     0
Paper:    1
Scissors: 2

def winner(p1, p2):
    if (p1+1) % 3 == p2:
        return "Player 2 won because their move is one greater than player 1"
    elif p1 == p2:
        return "It's a draw because both players played the same move"
    else:
        return "Player 1 wins because we know that it's 
                not a draw and that player 2 didn't win"
"""
