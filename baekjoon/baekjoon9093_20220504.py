import sys

n = int(input()) # 테스트 케이스 개수

for i in range(n):
    str_list = sys.stdin.readline().strip().split() # 공백 제거 및 문자열 나눔으로 리스트 저장
    reverse_list = []
    
    for s in str_list: # 각 문자를 뒤집기
        reverse_list.append(s[::-1])
        
    result = ' '.join(reverse_list) # 공백을 넣어서 한 문자열로 합침
    print(result) # 각 줄마다 출력