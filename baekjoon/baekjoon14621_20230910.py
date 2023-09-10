import sys
input = sys.stdin.readline

n, m = map(int, input().split())
school = list(input().split())
root_list = [i for i in range(n+1)] # 부모노드를 저장하는 리스트
d_list = [list(map(int, input().split())) for _ in range(m)]
d_list.sort(key=lambda x: x[2]) # 학교간 거리를 기준으로 정렬

def find_root(x): # 부모 노드를 찾는 함수
    if root_list[x] != x:
        root_list[x] = find_root(root_list[x])
    return root_list[x]

answer = 0
cnt = 0
for u, v, d in d_list:
    u_root = find_root(u)
    v_root = find_root(v)
    if u_root != v_root and school[u-1] != school[v-1]: # 부모 노드가 다른지 + 성별이 다른지
        if u_root > v_root:
            root_list[u_root] = v_root
        else:
            root_list[v_root] = u_root
        answer += d
        cnt += 1

if cnt == n-1: # 모든 학교를 연결하는 경로가 없는 경우
    print(answer)
else:
    print(-1)