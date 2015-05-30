from mystery_word.py import game


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


# Tests
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
