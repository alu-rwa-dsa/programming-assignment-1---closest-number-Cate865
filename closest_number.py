#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    sorted_array = sorted(arr)
    close_num_list = []
    differences = []

    for num in range(0, len(sorted_array) - 1):
        diff = sorted_array[num + 1] - sorted_array[num]
        differences.append(diff)
        least_no = differences[0]

    for difference in differences:
        if difference < least_no:
            least_no = difference
    for num in range(0, len(sorted_array) - 1):
        diff = sorted_array[num + 1] - sorted_array[num]
        if least_no == diff:
            close_num_list.append(sorted_array[num])
            close_num_list.append(sorted_array[num + 1])

    return close_num_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
