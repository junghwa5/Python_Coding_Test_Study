n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[1], arr[0] + arr[1]))
elif n == 3:
    print(max(arr[0] + arr[2], arr[1] + arr[2]))
else:
    score = [0] * n
    score[0] = arr[0]
    score[1] = max(arr[1], arr[0] + arr[1])
    score[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    for i in range(3, n):
        score[i] = max(arr[i] + arr[i-1] + score[i-3], arr[i] + score[i-2])
    
    print(score[n-1])