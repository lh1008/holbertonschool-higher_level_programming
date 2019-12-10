#!/usr/bin/python3
for me in range(10):
    for run in range(10):
        if me < run:
            print('{:d}{:d}'.format(me, run), end=', ')
        if me == 8 and run == 9:
            print('{:d}{:d}'.format(me, run))
