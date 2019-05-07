def mutate_string(string, position, character):
    z=s[:position]
    z=z+character
    z=z+s[position+1:]
    return z

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)v
