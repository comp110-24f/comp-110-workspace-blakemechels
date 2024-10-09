"""Concatenation program"""

__author__: str = "730734783"


def concat(word01: str, word02: str) -> str:
    """Return concatation of two input strings"""
    return word01 + word02


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
