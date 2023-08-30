#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total=len(arr)
    count0=0
    countp=0
    countn=0
    for i in arr:
        if (i==0):
            count0+=1
        elif(i>0):
            countp+=1
        else:
            countn+=1
    print(countp/total)
    print(countn/total)
    print(count0/total)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
