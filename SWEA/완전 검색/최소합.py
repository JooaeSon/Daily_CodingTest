def dfs(i, j):
    global Sum, result

    if i == N - 1 and j == N - 1:
        if result >= Sum:
            result = Sum
        return

    # 오른쪽으로 갈 경우
    if j + 1 < N:
        Sum += lst[i][j + 1]
        dfs(i, j + 1)
        Sum -= lst[i][j + 1]
    # 아래로 갈 경우
    if i + 1 < N:
        Sum += lst[i + 1][j]
        dfs(i + 1, j)
        Sum -= lst[i + 1][j]


T = int(input())

for test_case in range(1, T + 1):
    result = float('inf')
    N = int(input())

    lst = [list(map(int, input().split())) for i in range(N)]
    Sum = lst[0][0]

    dfs(0, 0)

    print(f'#{test_case} {result}')
