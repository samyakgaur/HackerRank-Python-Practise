if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    #calculating the avg 
    
    a=sum(student_marks[query_name])/3
    
    #making sure that it prints as xy.00 and not xy.0
    
    print('{0:.2f}'.format(a))
