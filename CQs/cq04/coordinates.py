"""Coordinates program"""

__author__: str = "730734783"


def get_coords(xs: str, ys: str) -> None:
    """Print formatted pairs of each character in two input strings"""
    idxx: int = 0
    while idxx < len(xs):
        idxy: int = 0
        while idxy < len(ys):
            print(xs[idxx] + "," + ys[idxy])
            idxy = idxy + 1
        idxx += 1
