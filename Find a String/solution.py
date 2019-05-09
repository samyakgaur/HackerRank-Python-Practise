def count_substring(string, sub_string):
    count=0 
    #we can also run loop till len(string) but for more efficiency use the following :
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count 

if __name__ == '__main__':
