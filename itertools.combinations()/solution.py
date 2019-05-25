from itertools import combinations
s,n=input().split()
i=1
s=list(s)
s.sort()
for i in range(1,int(n)+1):
    l=list(combinations(s,i))
    for j in l:
        ans=''.join(j)
        print(ans)
