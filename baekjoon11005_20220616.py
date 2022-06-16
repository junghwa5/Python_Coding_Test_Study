import sys
input = sys.stdin.readline

n, b = map(int, input().split())
conv = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return conv[r]
    else:
        return convert(q, base) + conv[r]

print(convert(n, b))