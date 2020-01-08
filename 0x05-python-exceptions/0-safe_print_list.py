#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try:
                j = 0
                for i in range(x):
                        j += 1
                        print('{}'.format(my_list[i]), end='')
                print()
                return j
        except IndexError:
                return j
