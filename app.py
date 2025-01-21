from memory_game import play as memory_game_play
from guess_game import play as guess_game_play
from currency_roulette_game import play as currency_roulette_play
from score import add_score

def welcome():
    username = input('please insert your name:\n')
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')



def start_play():
    game_type = input('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to
    guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS:\n''')

    while True:

        if not game_type.isdigit():
            game_type = input('Please enter an actual number:\n')
            continue
        elif int(game_type) not in range(1, 4):
            game_type = input('The number must be 1, 2, or 3:\n')
            continue
        else:

            difficulty_level = input('Please choose game difficulty from 1 to 5:\n')

            while True:
                # Validate difficulty level input
                if not difficulty_level.isdigit():
                    difficulty_level = input('Please enter an actual number\n')
                    continue
                elif int(difficulty_level) not in range(1, 6):
                    difficulty_level = input('The number must be from 1 to 5\n')
                    continue
                else:
                    difficulty_level = int(difficulty_level)  # Convert to integer
                    break

            if game_type == '1':  # Memory Game
                if memory_game_play(difficulty_level):  # If user wins
                    add_score(difficulty_level)  # Add score based on difficulty
            elif game_type == '2':  # Guess Game
                if guess_game_play(difficulty_level):  # If user wins
                    add_score(difficulty_level)  # Add score based on difficulty
            elif game_type == '3':  # Currency Roulette
                if currency_roulette_play(difficulty_level):  # If user wins
                    add_score(difficulty_level)  # Add score based on difficulty

            break
