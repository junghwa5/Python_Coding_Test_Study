while True:
    try:
        string = input()
        result = [0, 0, 0, 0]
        for s in string:
            if s.islower(): # 소문자인 경우
                result[0] += 1
            elif s.isupper(): # 대문자인 경우
                result[1] += 1
            elif s.isdigit(): # 숫자인 경우
                result[2] += 1
            elif s.isspace(): # 공백인 경우
                result[3] += 1
        print(*result)
    except EOFError:
        break