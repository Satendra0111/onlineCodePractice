#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minSum=0
    maxSum=0
    for i in range(0,len(arr)-1,1):
        minSum+=arr[i]
    for i in range(1,len(arr),1):
        maxSum+=arr[i]
    
    print(minSum, maxSum)    
    
        
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
