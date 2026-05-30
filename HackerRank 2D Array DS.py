
import math
import os
import random
import re
import sys

def hourglassSum(a):
    maxs=float('-inf')
    s=0
    for i in range(4):
        for j in range(4):
            s=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
            maxs=max(maxs,s)
    return maxs
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
