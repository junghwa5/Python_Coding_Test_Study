import sys
input = sys.stdin.readline

s, e, q = input().split()
s = s.replace(":", "")
e = e.replace(":", "")
q = q.replace(":", "")
check_list1 = set() # 개강총회 입장 획인된 사람
check_list2 = set() # 개강총회 퇴장 확인된 사람 
while True:
    inp = input()
    if len(inp) < 5:
        break
    t, name = inp.split()
    t = t.replace(":", "")
    # 개강총회 시작 전 채팅한 사람
    if t <= s:
        check_list1.add(name)
    # 입장이 확인되었고 개강총회 종료 후 스트리밍 종료전까지 채팅한 사람
    if name in check_list1 and t >= e and t <= q:
        check_list2.add(name)

print(len(check_list2))