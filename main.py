import os
import sys
import time
import random
from termcolor import cprint, colored


REL_PATH = os.path.dirname(__file__)
FILES = [f for f in os.listdir(REL_PATH) if os.path.isfile(os.path.join(REL_PATH, f)) and f not in ["LICENSE", "README.md"] and not f.endswith(".py")]
APP_NAME = "PYRDLE"
VERSION = "1.4.1"
word_file = None


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


# os.system('mode con: cols=22 lines=14')
# TODO: Fix automatic console window resizing

ask_wordset()
with open(word_file) as f:
    words = [word.strip("\n") for word in f.readlines()]

answer = random.choice(words)

# DEBUG, COMMENT OUT
# answer = input()

correct_letters = 0
guesses = 6
char_list = [" "] * 5
answer_list = []
guess_list = []


def take_guess():
    global answer_list, guess_list, guesses
    guess = input().lower()
    answer_list = [ltr for ltr in answer]
    guess_list = [ltr for ltr in guess]
    if guess == "?????":
        return True
    if len(guess) == 5 and guess in words:
        for index in range(5):
            if answer[index] == guess[index]:
                char_list[index] = colored(guess[index].upper(), "grey", "on_green")
                answer_list[index] = 0
                guess_list[index] = None
        for index, char in enumerate(guess_list):
            if char in answer_list:
                char_list[index] = colored(guess[index].upper(), "grey", "on_yellow")
                answer_list[answer_list.index(char)] = 0
                guess_list[index] = None
        for index, char in enumerate(guess_list):
            if char:
                char_list[index] = colored(guess[index].upper(), "grey", "on_white")
        cprint(f"\033[1A{''.join(char_list)}")
        guesses -= 1
    elif len(guess) != 5:
        cprint("\033[1AFIVE!", "grey", "on_red", end="")
        print(" " * (len(guess) - 5) if len(guess) > 5 else "", end="\r")
        time.sleep(1)
        print("     ", end="\r")
    else:
        cprint("\033[1AINVAL", "grey", "on_red", end="\r")
        time.sleep(1)
        print("     ", end="\r")


clear_console()

cprint(f"{APP_NAME}", "grey", "on_green", end="")
cprint(f"v{VERSION}", "grey", "on_yellow", end="")
cprint(f"{word_file}\n", "grey", "on_white")

while guesses:
    if take_guess() or answer_list == [0, 0, 0, 0, 0]:
        break
print()
if answer_list != [0, 0, 0, 0, 0]:
    cprint("WORD:", "grey", "on_magenta")
    cprint(answer.upper(), "grey", "on_cyan")
