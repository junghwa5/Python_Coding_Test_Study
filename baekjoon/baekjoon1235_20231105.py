import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input().rstrip())

t = len(n_list[0]) # 학생 번호 길이
for i in range(1, t+1): # 뒷자리부터 비교하여 모든 학생이 다르면 멈춤
    temp = []
    for j in range(n):
        temp.append(n_list[j][-i:])
    if len(temp) == len(list(set(temp))):
        print(i)
        break