"""Summing the elements of a list using different loops"""

__author__: str = "730734783"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    total: float = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:
    total: float = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    total: float = 0.0
    for idx in range(0, len(vals)):
        total += vals[idx]
        idx += 1
    return total
