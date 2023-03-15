from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        c_list = []
        for o in orders:
            c_list += list(combinations(sorted(o), c))
        counter = Counter(c_list)
        if counter and counter.most_common()[0][1] >= 2:
            for con in counter.most_common():
                if con[1] == counter.most_common()[0][1]:
                    answer.append(''.join(con[0]))
    
    return sorted(answer)