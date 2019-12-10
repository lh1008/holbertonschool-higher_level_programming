#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        reak = abs(number) % 10
    else:
        reak = number % 10
    print(reak, end="")
    return reak
