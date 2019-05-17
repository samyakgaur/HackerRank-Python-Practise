#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
from datetime import timedelta

datetimeFormat = '%a %d %b %Y %H:%M:%S %z'

def time_delta(t1, t2):
    diff = abs(datetime.datetime.strptime(t1, datetimeFormat)- datetime.datetime.strptime(t2, datetimeFormat))
    secs = diff.total_seconds()
    # print(secs)
    return str(int(secs))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
