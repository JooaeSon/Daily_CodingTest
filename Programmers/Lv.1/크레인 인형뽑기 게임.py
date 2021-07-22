def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        for row in range(len(board)):
            if board[row][move - 1]:
                if basket and board[row][move - 1] == basket[-1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[row][move - 1])
                board[row][move - 1] = 0
                break

    return answer