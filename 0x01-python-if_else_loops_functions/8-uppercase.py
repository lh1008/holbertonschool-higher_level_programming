#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        make = ord(letter)
        if make in range(97, 123):
            make = make - 32
        print("{:c}".format(make), end='')
    print()
