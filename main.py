# Lab02cvst.py
# This program estimates the square root of a positive number, to at least n decimal places (default 4).
# Evin Lodder 9/22/22
import math


def square_root(num: float, decimal_places: int = 4) -> float:
    # special cases
    if num == 0:
        return 0
    if num == 1:
        return 1
    # binary search algo
    left: float = 0
    right: float = num + 1 # +1 is in case of decimal numbers: e.g. sqrt(0.05) = 0.22
    while left < right:
        midpoint: float = (left + right) / 2
        rounded: float = round(midpoint * midpoint, decimal_places)
        if rounded < num:
            left = midpoint
        elif rounded > num:
            right = midpoint
        else:
            return midpoint
    return left
            

def main() -> None:
    number: float = eval(input("Enter a positive number: "))
    sqrt: float = square_root(number)

    print("Program Sqrt Result:   ", sqrt)
    print("Python math.sqrt     :   ", math.sqrt(number))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
