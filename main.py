from choices import get_users_choice, get_system_choice,\
    find_winner, update_score
from data import score
from time import sleep


def menu(func):
    def warp():
        username = str()

        if score['user'] == 0 and score['system'] == 0:
            print('Welcome To Rock Paper Scissors')
            print(f'Please wait for loading game...')
            sleep(3)

        username = input('Enter your name: ').title()
        rounds = int(input('How many rounds is each game? '))
        result = func(rounds, username)

        return result
    return warp


@menu
def play(rounds, username):
    result = {'user': 0, 'system': 0}

    while result['user'] < rounds and result['system'] < rounds:
        user_choice = get_users_choice(username)
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice, result)

        print(f'{username}: {user_choice} System: '
              f'{system_choice} result: {winner}')

    update_score(result, rounds, username, winner)
    play_again = input('if you want play again press(y) or for exit press(q): ')

    if play_again == 'y':
        return play()

    print('see you')


play()
