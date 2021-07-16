###
#-------------------------------------------------------------------------------
# mario.py
#-------------------------------------------------------------------------------
#
# make pyramid of hashes
#
# Gemaakt door: Susanne Becker
#
###

from cs50 import get_int


def main():
    # request height input from user
    while True:
        height = get_int("Height: ")
        if height >= 0 and height <= 23:
            break

    #for loop for hashes and spaces
    for i in range(1, height + 1):
        hashes = i + 1
        spaces = height - i

        print(" " * spaces, end="")
        print("#" * hashes)


if __name__ == "__main__":
    main()