word = input()
result = ''

for w in word:
    if w.islower(): # 알파벳 소문자
        asc = ord(w) + 13
        if asc > 122:
            asc -= 26
        result += chr(asc)
    elif w.isupper(): # 알파벳 대문자
        asc = ord(w) + 13
        if asc > 90:
            asc -= 26
        result += chr(asc)
    else: # 그 외
        result += w
        
print(result)