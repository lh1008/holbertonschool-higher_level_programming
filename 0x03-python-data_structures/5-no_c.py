#!/usr/bin/python3
def no_c(my_string):

    c = ['c', 'C']
    string = my_string.translate({ord(c): '' for c in c})
    return string
