"""Making List Utility Functions!"""

__author__: str = "730734783"


def all(my_list: list[int], my_int: int) -> bool:
    idx: int = 0  # for running through each value of the list
    while idx < len(my_list):
        if my_list[idx] != my_int:  # have to specify idx of list not just idx
            return False  # allows for immediate exit if any value is not equal
        else:
            idx += 1  # progresses while loop
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # makes sure the list is not blank
    largest: int = 0  # lets something be set as largest value
    idx: int = 0
    while idx < len(input):
        if input[idx] > largest:
            largest = input[idx]  # sets new largest value
        idx += 1
    return largest  # once sure of largest, returns it


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        raise ValueError(
            "is_equal lists must be equal in length"
        )  # verifies lists are equal in length
    idx: int = 0
    while idx < len(
        list1
    ):  # since they are equal in length only need to check with one
        if list1[idx] != list2[idx]:  # checks each index of list for equality
            return False  # exits as soon as anything is not equal
        else:
            idx += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    idx: int = 0
    while idx < len(list_2):  # makes sure to run through every index being added
        list_1.append(list_2[idx])  # adds specified value at idx to other list
        idx += 1  # progresses while loop
