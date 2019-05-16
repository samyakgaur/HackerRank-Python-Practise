from itertools import permutations
l=[]
s,n=input().split()
l=list(permutations(s,int(n)))
l.sort() 
l.sort(key = len) 
j=1
for i in range(len(l)):
    for j in range(int(n)):
        print(l[i][j],end="")
    print()
