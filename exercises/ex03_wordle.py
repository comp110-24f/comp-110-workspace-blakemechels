"""Making my own Worlde game!"""

__author__: str = "730734783"


def main(secret: str) -> None:  # runs everything together
    """Entry to the program and main game loop!"""
    number_of_turns: int = 6  # set limit for number of turns
    index: int = 0
    turns: int = 1
    win: bool = False
    while index < number_of_turns and not win:  # keeps track of limit within turns
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))  # calls input_guess function function
        print(
            emojified(guess, secret)
        )  # expresses emojis with correct and wrong guesses
        if guess == secret:
            win = True
            print(
                f"You won in {turns}/6 turns!"
            )  # f notation makes concatenation easier
            return None
        turns += 1
        index += 1
    if not win:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(sw_len: int) -> str:
    gw: str = input(f"Enter a {sw_len} character word: ")  # f string usage
    while len(gw) != sw_len:  # makes sure length matches
        gw = input(
            f"That wasn't {sw_len} chars! Try again: "
        )  # says error and prompts redo until true
    return gw


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check whether character exists in string"""
    assert len(char_guess) == 1  # uses assertion
    idx: int = 0
    is_char: bool = False  # default is that the char is not in the guess
    while idx < len(secret_word):  # checks each character
        if secret_word[idx] == char_guess:
            is_char = True  # returns verified confirmation that char is in guess
        idx += 1
    return is_char  # returns default


WHITE_BOX: str = "\U00002B1C"  # global variables to use emojis
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Return emojis based on string matches"""
    assert len(guess) == len(secret)
    sec_idx: int = 0
    gus_idx: int = 0  # seperate index for guess
    emojis: str = ""
    while sec_idx < len(secret):
        char: str = secret[sec_idx]
        if char == guess[gus_idx]:
            emojis += GREEN_BOX  # green box to indicate match between guess and secret
        elif contains_char(secret, guess[gus_idx]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX  # establushed guessed char is false
        gus_idx += 1  # adds to index to keep the program progressing throught the chars of each
        sec_idx += 1  # adds to index to keep the program progressing throught the chars of each
    return emojis


if __name__ == "__main__":
    main(secret="codes")
