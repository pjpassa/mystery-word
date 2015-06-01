from mystery_word import display_text, handle_input, get_difficulty, \
    play_again, guess_checker, win_or_lose, final_message
from collections import defaultdict
import random
import os


# Functions

# Get word length.
def get_word_length(difficulty):
    if difficulty == 1:
        return random.randint(4, 6)
    elif difficulty == 2:
        return random.randint(6, 10)
    return random.randint(10, 15)


# Get initial word list.
def get_init_list(word_length):
    with open("/usr/share/dict/words") as f:
        word_list = f.readlines()
    return [word[:-1].lower() for word in word_list
            if len(word) - 1 == (word_length)]


# Returns a dictionary of counts of letter found at index
def letter_location_histogram(word_list, match_letter):
    histogram = defaultdict(int)
    for word in word_list:
        for index, letter in enumerate(word):
            if letter == match_letter:
                histogram[index] += 1
    return dict(histogram)


# Takes a dictionary and returns a list of tuples of the top number of words.
def top_items(dictionary, number):
    pair_list = [pair for pair in dictionary.items()]
    pair_list.sort(key=lambda pair: -pair[1])
    return pair_list[:number]


# Returns a list that contains the most words based on index of the letter.
def refine_list(word_list, letter):
    matching_words = [word for word in word_list if letter in word]
    non_matching_words = [word for word in word_list if letter not in word]
    letter_dict = letter_location_histogram(matching_words, letter)
    letter_dict[-1] = len(non_matching_words)
    top_index = top_items(letter_dict, 1)[0][0]
    if top_index == -1:
        return non_matching_words
    return [word for word in matching_words if letter == word[top_index]]


# Ensures that the words in the list match the current display.
def correct_list(word_list, current_word, guessed, letters):
    new_list = []
    for word in word_list:
        keep = True
        for index, letter in enumerate(word):
            if guessed[index] and letter != current_word[index]:
                keep = False
            elif not guessed[index] and letter in letters:
                keep = False
        if keep:
            new_list.append(word)
    return new_list


# The game!
def game(lives=8):
    difficulty = get_difficulty()
    word_list = get_init_list(get_word_length(difficulty))
    word = random.choice(word_list)
    guessed = [False for letter in word]
    letters = ""
    print("Try to guess the mystery word!")
    print("The word is {} letters long.".format(len(word)))
    input("Press Enter to cotinue.")
    os.system("clear")
    while True:
        print("\nThe current word is...\n")
        print(display_text(word, guessed))
        print("\nLives left: {}".format(lives))
        letter = handle_input(letters)
        letters += letter + " "
        word_list = refine_list(word_list, letter)
        word = random.choice(word_list)
        matched_indexes = guess_checker(word, letter)
        if matched_indexes:
            print("\nYes, {} is in the word!".format(letter))
            for index in matched_indexes:
                guessed[index] = True
        else:
            print("\nSorry, {} is not in the word.".format(letter))
            lives -= 1
        word_list = correct_list(word_list, word, guessed, letters)
        result = win_or_lose(guessed, lives)
        if result is None:
            continue
        print(final_message(result))
        print("\nThe word was {}.\n".format(word))
        break
    return play_again()


# Main program
if __name__ == "__main__":
    while game():
        continue
    print("\nThanks for playing!\n")
