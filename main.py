import random
from termcolor import cprint


with open("words") as f:
    words = [word.strip("\n") for word in f.readlines()]

# DEBUG WORD
# answer = "atoll"

# FOR NORMAL OPERATION
answer = random.choice(words)

correct_letters = 0
guesses = 6


def take_guess():
    global correct_letters, guesses
    answer_iter = answer
    guess = input().lower()
    if len(guess) == 5 and guess in words:
        for index, letter in enumerate(guess):
            if letter == answer_iter[index]:
                cprint(letter, "grey", "on_green", end="")
                letter_array = [ltr for ltr in answer_iter]
                letter_array[index] = " "
                answer_iter = "".join(letter_array)
                correct_letters += 1
            elif letter in answer_iter:
                cprint(letter, "grey", "on_yellow", end="")
                letter_array = [ltr for ltr in answer_iter]
                letter_array[index] = " "
                answer_iter = "".join(letter_array)
            else:
                cprint(letter, "grey", "on_white", end="")
        if guess == answer:
            exit()
        print()
        guesses -= 1
    elif len(guess) != 5:
        cprint("NOT5L", "grey", "on_red")
    else:
        cprint("INVAL", "grey", "on_red")
    correct_letters = 0


while guesses:
    take_guess()
    if correct_letters == 5:
        break
