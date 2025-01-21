import os
from utils import SCORES_FILE_NAME

# Constants
POINTS_OF_WINNING = 0

def add_score(difficulty):
    """
    Adds score based on the difficulty level.
    The points for winning a game are calculated as: (difficulty * 3) + 5.
    If the score file does not exist, it creates it and starts the score at the calculated points.
    """

    global POINTS_OF_WINNING
    POINTS_OF_WINNING = (difficulty * 3) + 5

    if os.path.exists(SCORES_FILE_NAME):
        try:

            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        except ValueError:

            print("Error reading the score. Starting with 0.")
            current_score = 0
    else:

        current_score = 0

    current_score += POINTS_OF_WINNING

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(current_score))

    print(f"Score updated! Current score: {current_score} points.")
