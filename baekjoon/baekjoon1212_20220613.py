import sys
input = sys.stdin.readline

n8 = int(input(), 8)
n2 = format(n8, 'b') # 2진수 - 'b', 8진수 - 'o', 16진수 - 'h'

print(n2)