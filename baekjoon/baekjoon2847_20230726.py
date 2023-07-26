n = int(input())
problem = []
for _ in range(n):
    problem.append(int(input()))
problem.reverse() # 리스트 거꾸로

# 리스트가 내림차순 정렬된 형태가 되도록 해야 함
cnt = 0
for i in range(1, n):
    # 점수가 같은 경우 -> 낮은 레벨의 점수 1 감소
    if problem[i-1] == problem[i]:
        problem[i] -= 1
        cnt += 1
    # 낮은 레벨의 점수가 더 큰 경우 -> 낮은 레벨의 점수가 (높은 레벨의 점수 - 1)이 되도록 설정
    elif problem[i-1] < problem[i]:
        cnt += (problem[i] - problem[i-1] + 1)
        problem[i] = problem[i-1] - 1

print(cnt)