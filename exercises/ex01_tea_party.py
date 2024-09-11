"""A program which will help with the planning of an amazing tea party!"""

__author__: str = "730734783"


def main_planner(
    guests: int,
) -> (
    None
):  # allows me to call all the functions in my program #No return type necessary
    """Entry point to my program"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # important to turn guests from integer to string so it can be combined
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # include keyword argument to input guests as people
    print(
        "Treats: " + str(treats(people=guests))
    )  # print result of calling treats with people=guests
    print(  # program automatically shuffles the lines like this for formatting
        "Cost: $"
        + str(
            cost(
                tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
            )  # call tea_bags and treats to use as arguments becuase they are not previously defined
        )
    )


# overall, prints and calls all of the functions defined below


def tea_bags(people: int) -> int:
    """Find the number of tea bags needed based on number of people."""
    return people * 2  # returning 2x the number of people that are inputted


def treats(people: int) -> int:
    """Find number of treats needed based on number of tea bags"""
    return int(tea_bags(people=people) * 1.5)  # keyword argument is important


# calls tea_bags function    #important to conver to int after multiplication by a float


def cost(tea_count: int, treat_count: int) -> float:
    """Find price based on treat and tea count"""
    return tea_count * 0.5 + treat_count * 0.75  # multiply first by PEMDAS


if __name__ == "__main__":  # allows for program to be runable
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# prompts for guest count instead of requiring function name in call
