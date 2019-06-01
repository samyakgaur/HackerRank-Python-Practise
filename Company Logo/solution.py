#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = sorted(input())
    r=Counter(s)
    #print(r)
    h=r.most_common(3)
    for i in h:
        print(i[0],i[1])

