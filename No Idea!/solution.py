happiness=0
n,m=map(int,input().split())
array=input().split()
seta=set(input().split())
setb=set(input().split())
#creates a list of 1,-1 
print(sum([(i in seta) - (i in setb) for i in array]))
