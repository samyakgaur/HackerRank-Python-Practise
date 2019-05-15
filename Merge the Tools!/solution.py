def merge_the_tools(string, k):
    #commented code failed 7 cases 
    # l=0
    # m=k
    # for i in range (k%len(string)+l):
    #     s=string[l:m]
    #     m=m+k
    #     l=k+l
    #     #s="".join(set(s))
    #     s=''.join([j for i,j in enumerate(s) if j not in s[:i]])
    #     print(s)
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
