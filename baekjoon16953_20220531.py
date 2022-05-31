a,b = map(int,input().split())
result = 1

while b != a:
    if b < a:
        result = -1
        break
    if b % 2 == 0:
        b = b // 2
        result += 1
    elif b % 10 == 1:
        b = b // 10
        result += 1
    else:
        result = -1
        break

print(result)