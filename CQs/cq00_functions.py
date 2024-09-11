"""My First Challenge Question"""

__author__ = "730734783"


def mimic(message: str) -> str:
    """Repeat input back to you!"""
    return message


def main() -> None:
    """Pulls together functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
