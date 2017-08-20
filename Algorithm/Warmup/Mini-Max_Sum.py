#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
print("{0} {1} ".format(sum(arr[:-1]),sum(arr[1:])))