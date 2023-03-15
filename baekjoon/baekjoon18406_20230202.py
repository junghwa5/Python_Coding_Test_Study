n = input()
l = len(n)
left = n[: l//2]
right = n[l//2 :]
l_num = 0
r_num = 0
for i in range(l//2):
    l_num += int(left[i])
    r_num += int(right[i])

if l_num == r_num:
    print("LUCKY")
else:
    print("READY")
