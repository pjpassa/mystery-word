from mystery_word import display_text
from mystery_word import handle_input
from mystery_word import get_difficulty
import random


# Functions

# Get word length.
def get_word_length(difficulty):
    if difficulty == 1:
        return random.randint(4, 7)
    elif difficulty == 2:
        return random.randint(6, 11)
    return random.randint(10, 15)


# Get initial word list.
def get_init_list(word_length):
    with open("/usr/share/dict/words") as f:
        word_list = f.readlines()
    return [word[:-1].lower() for word in word_list
            if len(word) - 1 == (word_length)]


# Refine new list with guess
def refine_list(word_list, letter):
    new_list = [word for word in word_list if letter in word]
    return new_list
