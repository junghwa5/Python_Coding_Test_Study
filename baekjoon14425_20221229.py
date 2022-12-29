n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
m_list = []
for _ in range(m):
    m_list.append(input())
    
answer = 0
for mm in m_list:
    if mm in s:
        answer += 1
        
print(answer)