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
def display_state(word, guessed):
    pass

# Handle input from user.

# End conditions check.

# Display result.


# Tests
assert_exists(pick_word())
assert_equals(display_state('banana', [True, False, True, False, True, False]),
              'b_n_n_')
