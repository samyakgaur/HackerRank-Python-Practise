from collections import deque
s=deque()
n=int(input())
for i in range(n):
    eval('s.{0}({1})'.format(*input().split()+['']))
for i in s:
    print(i,end=" ")
