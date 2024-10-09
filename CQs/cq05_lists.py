"""Mutating Functions"""

__author__: str = "730734783"


def manual_append(list: list[int], added: int) -> None:
    """Adds int to a list"""
    list.append(added)


def double(list1: list[int]) -> None:
    """Doubles each index of list"""
    idx: int = 0
    while idx < len(list1):
        list1[idx] = list1[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
