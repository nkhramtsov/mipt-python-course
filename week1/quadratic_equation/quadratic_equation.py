import sys
import math

if __name__ == "__main__":
    a, b, c = map(int, sys.argv[1:])
    discriminant = b ** 2 - 4 * a * c
    first_root = (- b - math.sqrt(discriminant)) / (2 * a)
    second_root = (- b + math.sqrt(discriminant)) / (2 * a)
    print(int(first_root), int(second_root), sep="\n")
