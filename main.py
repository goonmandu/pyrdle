import os
import sys
import time
import random
from termcolor import cprint, colored


REL_PATH = os.path.dirname(__file__)
WORDSET_PATH = f"{REL_PATH}/wordsets"
FILES = [f for f in os.listdir(WORDSET_PATH)
         if os.path.isfile(os.path.join(WORDSET_PATH, f))
         and not f.endswith((".txt", ".py"))]
APP_NAME = "PYRDLE"
VERSION = "2.1.0"
word_file = None
tries = 6


def clear_console():
    if os.name in ["nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")


def ask_in_console():
    global word_file
    clear_console()
    print(f"Wordsets: {', '.join(FILES)}")
    word_file = input("Pick a wordset: ")
    if word_file not in FILES:
        ask_in_console()


def ask_wordset():
    global word_file
    clear_console()
    if len(sys.argv) < 2:
        ask_in_console()
    elif sys.argv[1] in FILES:
        word_file = sys.argv[1]
    else:
        ask_in_console()


def print_app_header():
    cprint(f"{APP_NAME}", "grey", "on_green", end="")
    cprint(f"v{VERSION}", "grey", "on_yellow", end="")
    cprint(f"{word_file}\n", "grey", "on_white")


def evaluate_guess(guess, against) -> list[int]:
    guess = guess.lower()
    against = against.lower()
    letters_left_in_answer = [ltr for ltr in against]
    evaluation = [0] * len(against)
    # Check for green matches first so that yellows do not eat up green letters
    # Greens are 2, Yellows are 1, and Grays are 0
    for idx, ltr in enumerate(guess):
        if against[idx] == guess[idx] and ltr in letters_left_in_answer:
            evaluation[idx] = 2
            letters_left_in_answer.remove(ltr)
    for idx, ltr in enumerate(guess):
        # evaluation[idx] != 2 prevents existing greens from being overwritten with a yellow
        # when there are duplicate letters in the answer
        if ltr in against and ltr in letters_left_in_answer and evaluation[idx] != 2:
            evaluation[idx] = 1
            letters_left_in_answer.remove(ltr)
    return evaluation


ask_wordset()
with open(f"{WORDSET_PATH}/{word_file}") as f:
    words = [word.strip("\n") for word in f.readlines()]

answer = random.choice(words)
answerlen = len(answer)

clear_console()
print_app_header()

while True:
    # If the user has run out of tries,
    if tries == 0:
        # Show answer and exit
        cprint(answer.upper(), "grey", "on_magenta")
        break
    char_list = [] * answerlen
    user_guess = input()
    guesslen = len(user_guess)

    # If the user requests the answer,
    if user_guess == "?????":
        # Show answer and exit
        cprint(answer.upper(), "grey", "on_magenta")
        break

    # If the guess length is not appropriate,
    if len(user_guess) != answerlen:
        # Print warning and let user guess again
        cprint("\033[1ALNGTH" + " " * (answerlen - 5), "grey", "on_red", end="")
        print(" " * (guesslen - answerlen) if guesslen > answerlen else "", end="\r")
        time.sleep(1)
        print("     ", end="\r")
        continue

    # If the guessed word is not in the chosen wordset:
    if user_guess not in words:
        # Print warning and let user guess again
        cprint("\033[1AINVAL" + " " * (answerlen - 5), "grey", "on_red", end="\r")
        time.sleep(1)
        print(" " * answerlen, end="\r")
        continue

    # If the guess is a valid len(answer) letter word, evaluate
    result = evaluate_guess(user_guess, answer)
    tries -= 1

    # Format result string according to the list returned by evaluate_guess()
    for idx, value in enumerate(result):
        if value == 2:
            char_list.append(colored(user_guess[idx].upper(), "grey", "on_green"))
        elif value == 1:
            char_list.append(colored(user_guess[idx].upper(), "grey", "on_yellow"))
        else:
            char_list.append(colored(user_guess[idx].upper(), "grey", "on_white"))

    # Print result string
    cprint(f"\033[1A{''.join(char_list)}")

    # If the user guessed correctly,
    if result == [2] * answerlen:
        # Exit
        break
