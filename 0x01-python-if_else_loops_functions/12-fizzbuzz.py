#!/usr/bin/python3
def fizzbuzz():
    for me in range(1, 101):
        if me % 3 is 0 and me % 5 is 0:
            print("FizzBuzz ", end='')
        elif me % 3 is 0:
            print("Fizz ",  end='')
        elif me % 5 is 0:
            print("Buzz ", end='')
        else:
            print('{} '.format(me), end='')
