# Lab02cvst.py
# This program estimates the square root of a positive number, to at least n decimal places (default 4).
# Evin Lodder 9/22/22
import math


def square_root(num: float, decimal_places: int = 6) -> float:
    # have to be careful with decimal_places
    # each added decimal place makes program much slower
    # 6 seems to be a sweet spot of sorts

    # special cases
    if num == 0:
        return 0
    if num == 1:
        return 1
    # binary search algo
    left: float = 0
    right: float = num + 1  # +1 is in case of decimal numbers: e.g. sqrt(0.05) = 0.22
    while left < right:
        midpoint: float = (left + right) / 2
        # The only issue with this take is that when you have two very large decimals
        # like 1e-15, floating point arithmetics get innacurate
        # and so the program gets stuck on very large numbers
        rounded: float = round(midpoint * midpoint, decimal_places)
        if rounded < num:
            left = midpoint
        elif rounded > num:
            right = midpoint
        else:
            return round(midpoint, decimal_places)
    return left


def main() -> None:
    number: float = eval(input("Enter a positive number: "))
    # Negative check just in case
    if number < 0:
        print("That isn't a positive number!")
        return main()
    sqrt: float = square_root(number)

    print("Program Sqrt Result:   ", sqrt)
    print("Python math.sqrt   :   ", math.sqrt(number))


if __name__ == '__main__':
    main()