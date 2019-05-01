if __name__ == '__main__':
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    
    #returns second_highest = [37.2, 37.21, 39.0, 41.0] if [1] not specified 
    #but we need the second highest so we take the second element 
    
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
