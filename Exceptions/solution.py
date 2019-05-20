n=int(input())
for i in range(n):
    a,b=input().split()
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero") 
    except ValueError as v:
        print("Error Code:",v)
