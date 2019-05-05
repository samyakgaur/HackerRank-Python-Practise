def swap_case(s):
    n=''
    for i in s:
        if (i.isupper()) == True:
            n=n+i.lower()
        elif (i.islower()) == True:
            n=n+i.upper()
        else:
            n=n+i
    return n


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
