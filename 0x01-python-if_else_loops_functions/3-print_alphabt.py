#!/usr/bin/python3
for chr in range(97, 123):
    if chr is 101 or chr is 113:
        continue
    print('{:c}'.format(chr), end='')
