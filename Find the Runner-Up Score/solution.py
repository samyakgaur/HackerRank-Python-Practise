if __name__ == '__main__':
    n = int(input())
    
    #as map doesnt return a list we use sorted function to 
    #1)sort the map
    #2)return a list and store it in arr
    
    arr = sorted(map(int, input().split()))
    
    
    #we check if the last two numbers in the list are same or not
    #we delete the same largest number because we dont want to return a number equal to largest number
    #for example list = [1,2,3,6,6] so we want to return 3 not 6 
    #so we restructure the list to = [1,2,3,6] and then return the second last element 
    
    
    while(arr[len(arr)-1]==arr[len(arr)-2]):
        max1=max(arr)
        arr.remove(max1)
    
    
    print(arr[len(arr)-2])
