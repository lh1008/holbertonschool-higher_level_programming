#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Method that sorts and prints list """
    if list_of_integers == []:
        return(None)
    else:
        return(max(list_of_integers))
