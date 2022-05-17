# pyrdle
CLI-based Python recreation of Wordle with color support.
Current wordsets include: `wordle`, `lewdle`, and the Stanford 5-letter word list (`stanford`).

Tested with Python 3.9 and 3.10.

# how to play
Run it in the terminal, like this:
```
PATH_TO_DIRECTORY/pyrdle/python3 main.py [wordset]
```
If no wordset argument is passed in, or the argument is not in the wordset list, the game will prompt you to choose a wordset.
Otherwise, the game will automatically start with the given wordset name.

You get 6 guesses. Entering `?????` will reveal the answer and end the round.

If you didn't know already, GREENS are exact matches, YELLOWS are in the answer but in a different spot, while GRAYS are not in the answer.

# dependencies
termcolor: `pip install termcolor`

# known bugs and fix status
- [x] Fixed: when calculating the answer, YELLOW and GREEN guesses are treated the same (as "0") and will make the game exit once every letter is at least a YELLOW.

# screenshots (outdated)
![image](https://user-images.githubusercontent.com/61984863/154415450-e43183c0-305b-4011-9b66-2041bf410f0d.png) ![image](https://user-images.githubusercontent.com/61984863/154416191-25872296-7056-43c3-8c0d-6fab9bd324b8.png)
![image](https://user-images.githubusercontent.com/61984863/154416556-862bfb4e-2414-47d3-9991-85bcfc1bf333.png)
