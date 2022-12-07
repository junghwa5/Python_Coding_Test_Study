n, k = map(int, input().split())
coin_li = []
for _ in range(n):
    coin_li.append(int(input()))
coin_li.reverse()
    
cnt = 0
for c in coin_li:
    cnt += k // c
    k %= c
    
print(cnt)