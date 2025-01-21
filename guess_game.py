import random

def genrate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    print(secret_number)
    return secret_number


def get_guess_from_user():
    while True:
        guess = input('Please guess a number between 1 to 5:\n')

        # Validate numbers
        if not guess.isdigit():
            print('Please enter an actual number.')

        # Validate range
        elif int(guess) not in range(1, 6):
            print('The number must be between 1 and 5.')

        else:
            return int(guess)  # Return the valid guess

def compare_results(computer_number, user_number):
    return computer_number == user_number


def play(difficulty=5):
    computer_number = genrate_number(difficulty)
    user_number = get_guess_from_user()
    result = compare_results(computer_number, user_number)
    if result:
        print('You won!')
    else:
        print(f'You lost! the correct number was : {computer_number}')
