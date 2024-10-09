"""Basic syntax of lists."""

# my_numbers: list[float] = []  # literal
# my_numbers: list[float] = list()  # constructer

# print(my_numbers)

# my_numbers.append(1.5)
# my_numbers.append(1.3)

# print(my_numbers)

game_points: list[int] = [102, 86, 94]

# print(game_points)


# print(game_points[2])

# game_points[1] = 72
# print(game_points)

# print(len(game_points))
# game_points.pop(1)
# print(game_points)


# Write a funtion called display


def display(list1: list[int]) -> None:
    idx: int = 0
    while idx < len(list1):
        print(list1[idx])
        idx += 1


# display(game_points)
game_points.append(94)
print(game_points)
