if __name__ == '__main__':
    n = int(input())
    t=()
    integer_list = map(int, input().split())
    
    #making the map object as list arg
    integer_list=tuple(integer_list)
    
    #converting list to tuple 
    t=tuple(integer_list)
    
    #printing 
    print(hash(t))
