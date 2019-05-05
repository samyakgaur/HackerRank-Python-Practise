def split_and_join(line):
    #split the string whenever a space is encountered 
    line=line.split(" ")
    #join the list using '-'
    line="-".join(line)
    return line
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
