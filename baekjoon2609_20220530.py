a, b = map(int,input().split())

# 최대 공약수
for i in range(min(a, b), 0, -1):
    if a%i == 0 and b%i == 0:
        print(i)
        break

# 최소 공배수
for j in range(max(a, b), a*b+1, max(a, b)):
    if j%a == 0 and j%b == 0:
        print(j)
        break