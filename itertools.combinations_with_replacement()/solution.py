from itertools import combinations_with_replacement
word, n = input().split()
for el in combinations_with_replacement(sorted(word),int(n)):
    print(*el, sep='')a
