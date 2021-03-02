T = int(input())

for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    memo = [[0] * (i + 1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(i + 1):
            if j == 0 or i == j:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

    print(f'#{test_case} {memo[n][b]}')
