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
    difficulty = None
    print("What difficulty do you want to play?")
    while True:
        input_text = "Enter 1 for easy, 2 for normal, or 3 for hard. > "
        difficulty_input = input(input_text)
        try:
            difficulty = int(difficulty_input)
        except ValueError:
            print("Please enter 1, 2, or 3.")
            continue
        if difficulty not in range(1, 4):
            print("Please enter 1, 2, or 3.")
            continue
        return difficulty


# Retrives a random word from /usr/share/dict/words
def retrieve_random_word():
    with open("/usr/share/dict/words") as f:
        word_list = f.readlines()
    return random.choice(word_list)[:-1]


# Picks a random word given a difficulty.
def pick_word(difficulty):
    word = ""
    if difficulty == 1:
        while len(word) not in range(4, 7):
            word = retrieve_random_word()
    elif difficulty == 2:
        while len(word) not in range(6, 11):
            word = retrieve_random_word()
    else:
        while len(word) < 10:
            word = retrieve_random_word()
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
        if letters:
            print("You have already guessed {}.".format(letters[:-1]))
        character = input("Guess a letter or enter 'quit' to quit. > ").lower()
        if character == "quit":
            print("\nThanks for playing!\n")
            exit()
        elif len(character) != 1 or not character.isalpha():
            print("Please enter only 1 letter.")
        elif character in letters:
            print("You have already chosen '{}'.".format(character))
        else:
            return character


# Returns a list with the matched indexes.
def guess_checker(word, letter):
    matched = []
    for index, character in enumerate(word):
        if letter == character:
            matched.append(index)
    return matched


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


# Checks if the player wants to play again.
def play_again():
    while True:
        response = input("Do you want to play again (y/n)? > ")
        if response.lower() in ['y', 'yes']:
            return True
        elif response.lower() in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")


# Game loop.
def game(lives=8):
    difficulty = get_difficulty()
    word = pick_word(difficulty)
    guessed = [False for letter in word]
    letters = ""
    print("Try to guess the mystery word!")
    print("The word is {} letters long.".format(len(word)))
    while True:
        print("\nThe current word is...\n")
        print(display_text(word, guessed))
        print("\nYou have {} lives left.".format(lives))
        letter = handle_input(letters)
        print("\n"*3)
        letters += letter + " "
        matched_indexes = guess_checker(word, letter)
        if matched_indexes:
            print("\nYes, {} is in the word!".format(letter))
            for index in matched_indexes:
                guessed[index] = True
        else:
            print("\nSorry, {} is not in the word.".format(letter))
            lives -= 1
        result = win_or_lose(guessed, lives)
        if result is None:
            continue
        print(final_message(result))
        print("\nThe word was {}.\n".format(word))
        break
    return play_again()

# Tests
"""
assert_exists(pick_word(2))
assert_equals(display_text('banana', [True, False, True, False, True, False]),
              'b _ n _ n _ ')
assert_equals(len(handle_input("")), 1)
assert_equals(win_or_lose([False, True, True], 0), False)
assert_equals(win_or_lose([True, True, True], 3), True)
assert_equals(win_or_lose([False, True, True], 3), None)
assert_equals(final_message(True), "Congratulations! You have won!")
assert_equals(final_message(False), "Sorry, you have lost.")

# assert_equals(game(pick_word(2), 8), True)
"""

while game():
    continue
print("\nThanks for playing!\n")
