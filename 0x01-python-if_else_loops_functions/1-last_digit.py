#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = number
str3 = "is"
if number < 0:
    str4 = abs(number) % 10
    if str4 == 0:
        str5 = '{} {} {} {}'.format(str1, str2, str3, str4)
    else:
        str5 = '{} {} {} -{}'.format(str1, str2, str3, str4)
else:
    str4 = number % 10
    str5 = '{} {} {} {}'.format(str1, str2, str3, str4)
if str4 > 5:
    print('{}'.format(str5), "and is greater than 5")
elif str4 == 0:
    print('{}'.format(str5), "and is 0")
elif str4 < 6:
    print('{}'.format(str5), "and is less than 6 and not 0")
