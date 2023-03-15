import sys

n = int(sys.stdin.readline())
qu = []

for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        qu.append(line[1])
    elif line[0] == 'pop':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu.pop(0))
    elif line[0] == 'size':
        print(len(qu))
    elif line[0] == 'empty':
        if len(qu) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[0])
    elif line[0] == 'back':
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[-1])