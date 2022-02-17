import os
import sys
import random
from termcolor import cprint, colored


REL_PATH = os.path.dirname(__file__)
FILES = [f for f in os.listdir(REL_PATH) if os.path.isfile(os.path.join(REL_PATH, f)) and f not in ["LICENSE", "README.md"] and not f.endswith(".py")]
APP_NAME = "PYRDLE"
VERSION = "1.2.4"
WORD_FILE = None


def clear_console():
    if os.name in ["nt", "dos"]:
        os.system("cls")
    else:
        os.system("clear")


def ask_in_console():
    global WORD_FILE
    clear_console()
    print(f"Wordsets: {', '.join(FILES)}")
    WORD_FILE = input("Pick a wordset: ")
    if WORD_FILE not in FILES:
        ask_in_console()


def ask_wordset():
    global WORD_FILE
    clear_console()
    if len(sys.argv) < 2:
        ask_in_console()
    elif sys.argv[1] in FILES:
        WORD_FILE = sys.argv[1]
    else:
        ask_in_console()


ask_wordset()
with open(WORD_FILE) as f:
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
        cprint("".join(char_list))
        guesses -= 1
    elif len(guess) != 5:
        cprint("FIVE!", "grey", "on_red")
    else:
        cprint("INVAL", "grey", "on_red")


clear_console()

cprint(f"{APP_NAME}", "grey", "on_green", end="")
cprint(f"v{VERSION}", "grey", "on_yellow", end="")
cprint(f"{WORD_FILE}\n", "grey", "on_white")

while guesses:
    if take_guess() or answer_list == [0, 0, 0, 0, 0]:
        break
print()
cprint("WORD:", "grey", "on_magenta")
cprint(answer.upper(), "grey", "on_cyan")
