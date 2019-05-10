import textwrap

def wrap(string, max_width):
    count=0
    for i in range(0,len(string)):
        if count is max_width:
            count=0 
            print("")
        print(string[i],end="")
        count+=1
        if i == len(string)-1:
            return " "

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
