import random
from termcolor import cprint, colored


with open("words") as f:
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


while guesses:
    take_guess()
    if answer_list == [0, 0, 0, 0, 0]:
        break
print()
cprint("WORD:", "grey", "on_magenta")
cprint(answer.upper(), "grey", "on_cyan")
