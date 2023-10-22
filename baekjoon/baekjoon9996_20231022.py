import sys
input = sys.stdin.readline

n = int(input())
p = input().split("*")
for _ in range(n):
    s = input()
    if len(s) >= (len(p[0]) + len(p[1])) and s[:len(p[0])] == p[0] and s[-len(p[1]):] == p[1]:
        print("DA")
    else:
        print("NE")