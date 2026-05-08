import math


CONSTANT = 3


def square(value):
    if value < 0:
        raise ValueError("value must be non-negative")
    return value * value


def hypotenuse(a, b):
    return math.sqrt(square(a) + square(b))


if __name__ == "__main__":
    print(hypotenuse(CONSTANT, 4))
