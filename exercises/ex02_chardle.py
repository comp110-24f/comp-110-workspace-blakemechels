"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730734783"


def main() -> None:  # allows for everything to be called easier
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    wor: str = input("Enter a 5-character word: ")
    if len(wor) != 5:  # checks if input is equal to 5 character lengthh
        print("Error: Word must contain 5 characters.")
        quit()  # exit the program if condition is not met
    return wor


def input_letter() -> str:
    char: str = input("Enter a single character: ")
    if len(char) != 1:  # make sure character is single
        print("Error: Character must be a single character.")
        quit()  # quit the program if condition is not met
    return char


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:  # works its way through each index of the word
        print(letter + " found at index 0")
        count += 1  # if condition is met, adds to the count which will eventually be printed.
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if (
        word[4] == letter
    ):  # final index necessary because the length is limited to five characters
        print(letter + " found at index 4")
        count += 1
    if count == 0:  # unique condition if count is 0
        print("No instances of " + letter + " found in " + word)
    if count == 1:  # careful of plurality of instances
        print(str(count) + " instance of " + letter + " found in " + word)
    if count > 1:  # string of variable allows flexibilty depending on count
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":  # calls main function
    main()
