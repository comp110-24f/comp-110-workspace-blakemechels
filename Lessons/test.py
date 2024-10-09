def func(word: str) -> str:
    idx: int = len(word) - 1
    while idx >= 0:
        print(word[idx])
        idx = idx - 1
    return word


func(word="blue")
