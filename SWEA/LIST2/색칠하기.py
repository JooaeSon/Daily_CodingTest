T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [[0 for _ in range(10)] for _ in range(10)]

    for _ in range(N):
        lst = list(map(int, input().split()))
        for i in range(lst[0], lst[2] + 1):
            for j in range(lst[1], lst[3] + 1):
                if lst[-1] == 1:
                    board[i][j] += 100
                elif lst[-1] == 2:
                    board[i][j] += 1

    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] > 100:
                cnt = cnt + 1
    result = cnt

    print(f'#{test_case} {result}')