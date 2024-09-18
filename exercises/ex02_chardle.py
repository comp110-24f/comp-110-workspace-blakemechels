"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730734783"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
    return word


def input_letter() -> str:
    char: str = input("Enter a single character: ")
    if len(char) != 1:
        print("Error: Character must be a single character.")
    return char

def contains_char(w: str, l: str) -> None:
