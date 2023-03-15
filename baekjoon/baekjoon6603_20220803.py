from itertools import combinations

while True:
    l_set = list(map(int, input().split()))
    if l_set[0] == 0:
        break
    else:
        l_set = l_set[1:]
        lotto = list(combinations(l_set, 6))
        for l in lotto:
            print(*l)
    print()