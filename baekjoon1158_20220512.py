n, k = map(int, input().split())
circle_list = list(range(1, n+1))
remove_list = []
idx = 0

for i in range(n):
    idx += k-1
    if idx >= len(circle_list):
        idx = idx % len(circle_list)
    remove_list.append(str(circle_list.pop(idx)))
        
print("<", end='')
for r in range(len(remove_list)):
    if r == len(remove_list)-1:
        print(remove_list[r], end='', sep='')
    else:
        print(remove_list[r], ", ", end='', sep='')
print(">")