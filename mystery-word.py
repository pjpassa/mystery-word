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


# Returns game difficulty.
def get_difficulty():
    print("What difficulty do you want to play?")
    difficulty_input = input("Enter 1 for easy, 2 for normal, or 3 for hard.")
    try:
        difficulty = int(difficulty_input)
    except ValueError:
        print("Please enter 1, 2, or 3.")
        return None
    if difficulty not in range(1, 4):
        print("Please enter 1, 2, or 3.")
        return None
    return difficulty


# Picks a random word.
def pick_word():
    difficulty = None
    while not difficulty:
        difficulty = get_difficulty()
    with open("/usr/share/dict/words") as f:
        word_list = f.readlines()
    word_length = range(0)
    if difficulty == 1:
        word_length = range(4, 7)
    elif difficulty == 2:
        word_length = range(6, 11)
    else:
        word_length = range(10, 100)
    word = random.choice(word_list)[:-1]
    while len(word) not in word_length:
        word = random.choice(word_list)[:-1]
    return word


# Display current state.
def display_text(word, guessed):
    string = ""
    for index, bool in enumerate(guessed):
        if bool:
            string += word[index] + " "
        else:
            string += "_ "
    return string


# Handle input from user.
def handle_input(letters):
    character = ''
    while True:
        print("You have already guessed {}.".format(letters[:-1]))
        character = input("Guess a letter or enter 'quit' to quit. > ").lower()
        if character == "quit":
            exit()
        elif len(character) != 1 or not character.isalpha():
            print("Please enter only 1 letter.")
        elif character in letters:
            print("You have already chosen '{}'.".format(character))
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
def final_message(result):
    if result:
        return "Congratulations! You have won!"
    return "Sorry, you have lost."


# Game loop.
def game(word, lives):
    guessed = [False for letter in word]
    letters = ""
    print("Try to guess the mystery word!")
    print("The word is {} letters long.".format(len(word)))
    while True:
        print("You have {} lives left.".format(lives))
        print("The current word is...")
        print(display_text(word, guessed))
        letter = handle_input(letters)
        letters += letter + " "
        correct = False
        for index, character in enumerate(word):
            if letter == character:
                guessed[index] = True
                correct = True
        if not correct:
            lives -= 1
        result = win_or_lose(guessed, lives)
        if result is None:
            continue
        print(final_message(result))
        print("The word was {}.".format(word))
        break
    return True

# Tests
"""
assert_exists(pick_word())
assert_equals(display_text('banana', [True, False, True, False, True, False]),
              'b _ n _ n _ ')
assert_equals(len(handle_input("")), 1)
assert_equals(win_or_lose([False, True, True], 0), False)
assert_equals(win_or_lose([True, True, True], 3), True)
assert_equals(win_or_lose([False, True, True], 3), None)
assert_equals(final_message(True), "Congratulations! You have won!")
assert_equals(final_message(False), "Sorry, you have lost.")

assert_equals(game(pick_word(), 8), True)
"""

while True:
    print("What difficulty do you want to play?")
    difficulty = input("Enter 1 for easy, 2 for normal, or 3 for hard.")
    if not difficulty.isdigit():
        print("I didn't understand that.")
        continue
    if int(difficulty) not in range(1, 4):
        print("I didn't understand that.")
        continue
    game(pick_word(int(difficulty)), 8)
    while True:
        response = input("Do you want to play again (y/n)? ")
        if response[0].lower() == 'y':
            break
        elif response[0].lower() == 'n':
            exit()
        print("I didn't understand that.")
