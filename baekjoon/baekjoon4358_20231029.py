import sys
from collections import Counter
input = sys.stdin.readline

tree_list = []
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    tree_list.append(tree)
    cnt += 1

c = sorted(Counter(tree_list).items())
for key, value in c:
    print("%s %.4f" %(key, value/cnt*100))