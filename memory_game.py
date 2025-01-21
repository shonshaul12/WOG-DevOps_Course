import random
import time
from utils import screen_cleaner, SCORES_FILE_NAME, BAD_RETURN_CODE
from score import add_score

def play_memory_game(difficulty):

    if user_wins:
        add_score(difficulty)


def generate_sequence(difficulty):
    sequence = [random.randint(1, 100) for _ in range(difficulty)]
    return sequence


def get_list_from_user(difficulty):
    print(f"Enter the sequence of {difficulty} numbers (separated by spaces):")
    while True:
        try:

            user_input = input("Your sequence: ")
            user_list = list(map(int, user_input.split()))

            if len(user_list) == difficulty:
                return user_list
            else:
                print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Please enter only numbers.")


def is_list_equal(original, user_input):
    # Compare the two lists (original and user input)
    return original == user_input


def play(difficulty):
    print("Welcome to the Memory Game!")

    sequence = generate_sequence(difficulty)

    print(f"Memorize this sequence: {sequence}")
    time.sleep(0.7)  # Wait for 0.7 seconds

    try:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    except Exception:
        pass

    user_input = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_input):
        print(f"Congratulations! You remembered the sequence correctly: {sequence}")
        return True
    else:
        print(f"Sorry, you lost! The correct sequence was: {sequence}")
        return False


# Main execution to start the game
if __name__ == "__main__":
    difficulty = int(input("Enter difficulty (1 to 10): "))
    if play(difficulty):
        print("You win!")
    else:
        print("You lose!")
