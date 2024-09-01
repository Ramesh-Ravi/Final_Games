import os

SCORES_FILE_NAME = r"C:\GH\Final_Project\Final_Games\Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')





