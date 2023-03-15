n = int(input())
num = 2

while True:
    if n == 1:
        break
        
    if n % num == 0:
        n = n // num
        print(num)
    else:
        num += 1