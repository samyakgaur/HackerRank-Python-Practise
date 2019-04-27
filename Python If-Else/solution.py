#!/bin/python3

n = int(input())
if n is not 0:
    if n%2 is not 0:
        print("Weird")
    elif n%2 is 0 and n<5:
        print("Not Weird")
    elif n%2 is 0 and n>5 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
