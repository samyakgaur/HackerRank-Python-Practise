from collections import Counter
l=[]
n=input()
for i in range(int(n)):
    l.append(input())
lc=Counter(l)
print(len(lc))
lv=list(lc.values())
for i in lv:
    print(i , end=" ")
