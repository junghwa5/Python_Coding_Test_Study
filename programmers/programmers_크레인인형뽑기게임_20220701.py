def solution(board, moves):
    answer = 0
    b_list = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                temp = board[i][m-1]
                board[i][m-1] = 0
                b_list.append(temp)
                if len(b_list) < 2:
                    break
                if b_list[-1] == b_list[-2]:
                    answer += 2
                    b_list.pop()
                    b_list.pop()
                break
    
    return answer