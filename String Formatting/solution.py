def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str("{0:2d}".format(i)).rjust(w,' '),end=" ")
        print(str("{0:2o}".format(i)).rjust(w,' '),end=" ")
        print(str("{0:2X}".format(i)).rjust(w,' '),end=" ")
        print(str("{0:2b}".format(i)).rjust(w,' '))

if __name__ == '__main__':
   n = int(input())
   print_formatted(n)
