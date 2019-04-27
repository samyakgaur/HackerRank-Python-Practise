def is_leap(year):
    leap = False
    
    if year%4 is 0 and year%100 is not 0 or year%400 is 0:
        leap= True 
    
    return leap

year = int(input())
print(is_leap(year))
