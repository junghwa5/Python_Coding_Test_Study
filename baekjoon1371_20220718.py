import sys
s = sys.stdin.read().replace("\n", "").replace(" ", "")
alpha = [0]*26

for str in s:
    alpha[ord(str) - ord('a')] += 1
    
for i in range(26):
    if alpha[i] == max(alpha):
        print(chr(i + ord('a')), end ='')