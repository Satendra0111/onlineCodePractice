#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours = int(s[0:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    am_pm = s[8:10]
    
    # Handle the case of 12:00:00AM and 12:00:00PM
    if hours == 12 and am_pm == 'AM':
        hours = 0
    elif hours == 12 and am_pm == 'PM':
        hours = 12
    else:
        # Add 12 to hours for PM times (except 12:00:00PM)
        hours = (hours + 12) % 24 if am_pm == 'PM' else hours
    
    # Format hours, minutes, and seconds to have leading zeros if needed
    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)
    
    military_time = f'{hours_str}:{minutes_str}:{seconds_str}'
    
    return military_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
