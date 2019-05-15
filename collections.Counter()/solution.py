#input the length of the list 
length=int(input())
l=[]
bill=0
#input the list 
l=input().split()
#input the number of customers
n=int(input())
for i in range(n):
    demand=input().split()
    #checking if he has the size and if yes we indicate is sold by replacing it with -1
    if demand[0] in l:
        place=l.index(demand[0])
        l[place]=-1
        bill=bill+int(demand[1])
print(bill)
