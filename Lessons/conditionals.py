"""Practiciing my Conditionals"""


def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2
    if num < 10:  # check if this is true
        print("small number")
    else:
        print("big number")
    print("this is the end of the function")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to comp 110"
    else:
        return "keep sleeping!!"

    # def check_first_letter(word: str, letter: str) -> str:
    """Return whether or not first letter matches words first letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match"


# print(check_first_letter(word="word", letter="r"))


def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("small number")
    else:
        print("big number")
    print("have a nice day!")


less_than_10(num=7)
