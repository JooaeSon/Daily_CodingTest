def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

    for i in range(row):
        for j in range(col):
            dp[i+1][j+1] = board[i][j]

    for i in range(1, row+1):
        for j in range(1, col+1):
            if dp[i][j] != 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    #print(max(map(int, max(dp)))** 2)
    return max(map(max, dp))**2