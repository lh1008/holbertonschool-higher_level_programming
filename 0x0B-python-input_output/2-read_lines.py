#!/usr/bin/python3
"""Module that reads lines oof a text file UTF8"""


def read_lines(filename="", nb_lines=0):
    """Method that read n lines of a text file UTF8"""
    with open('my_file_0.txt', encoding='utf-8') as file_name:
        nb_greater = len(file_name.read().split('\n')) - 1
        file_name.seek(0)
        if nb_lines <= 0 or nb_lines > nb_greater:
            print(file_name.read(), end='')
        else:
            for i in range(nb_lines):
                print(file_name.readline(), end='')
