n = int(input())
s_number = []
for _ in range(n):
    s_number.append(input())
    
def func(s_num):
    temp = 0
    for num in s_num:
        if num.isdigit():
            temp += int(num)
    return temp
    
s_number.sort(key = lambda x: (len(x), func(x), x))
for i in range(n):
    print(s_number[i])