from collections import deque

n = int(input())
tree = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
p_node = [0]*(n+1)

def bfs():
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for t in tree[node]:
            if p_node[t] == 0:
                queue.append(t)
                p_node[t] = node
                
bfs()
for p in p_node[2:]:
    print(p)