N, K = map(int, input().split())
a = []

for i in range(1, N+1):
    if N%i == 0:
        a.append(i)
        
if K <= len(a):
    print(a[K-1])
else:
    print(0)