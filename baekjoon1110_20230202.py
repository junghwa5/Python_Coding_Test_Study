N = int(input())

count = 1
if N < 10:
    num = N * 10 + N
else:
    num = (N % 10) * 10 + (N // 10 + N % 10) % 10
    
while N != num:
    if num < 10:
        num = num * 10 + num
    else:
        num = (num % 10) * 10 + (num // 10 + num % 10) % 10
    count += 1

print(count)
