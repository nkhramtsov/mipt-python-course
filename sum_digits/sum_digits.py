import sys

if __name__ == '__main__':
    digit_string = sys.argv[1]
    print(sum(map(int, digit_string)))
