import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    """
    Clears the terminal screen.
    Works on both Windows and Unix-based systems.
    """
    try:
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For Unix-based systems (Linux/Mac)
        else:
            os.system('clear')
    except Exception as e:
        print(f"Error clearing the screen: {e}")
