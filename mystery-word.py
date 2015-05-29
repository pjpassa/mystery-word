import random

# Functions


# Tests
# Takes two inputs and asserts that they equal each other
def assert_equals(input_one, input_two):
    try:
        assert input_one == input_two
    except AssertionError:
        raise AssertionError("Values don't match.")
    finally:
        print(".")


# Takes an input and asserts that it is not empty
def assert_exists(variable):
    try:
        assert variable
    except AssertionError:
        raise AssertionError("Value does not exist.")
    finally:
        print(".")


# Picks a random word.
def pick_word():
    with open("/usr/share/dict/words") as f:
        word_list = f.readlines()
    return random.choice(word_list)[:-1]


# Display current state.
def display_text(word, guessed):
    string = ""
    for index, bool in enumerate(guessed):
        if bool:
            string += word[index]
        else:
            string += "_"
    return string


# Handle input from user.
def handle_input():
    character = ''
    while True:
        character = input("Guess a letter or enter 'quit' to quit. > ").lower()
        if character == "quit":
            exit()
        elif len(character) != 1 or not character.isalpha():
            print("Please enter only 1 letter.")
        else:
            return character


# End conditions check.
def win_or_lose(guessed, lives):
    if lives == 0:
        return False
    victory = True
    for bool in guessed:
        victory = victory and bool
    if victory:
        return True
    return None


# Display result.


# Tests
assert_exists(pick_word())
assert_equals(display_text('banana', [True, False, True, False, True, False]),
              'b_n_n_')
assert_equals(len(handle_input()), 1)
assert_equals(win_or_lose([False, True, True], 0), False)
assert_equals(win_or_lose([True, True, True], 3), True)
assert_equals(win_or_lose([False, True, True], 3), None)
