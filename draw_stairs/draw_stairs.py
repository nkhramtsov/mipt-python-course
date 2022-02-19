import sys

if __name__ == "__main__":
    stairs_quantity = int(sys.argv[1])
    for sharp_amount in range(1, stairs_quantity + 1):
        print((stairs_quantity - sharp_amount) * " " + sharp_amount * "#")
