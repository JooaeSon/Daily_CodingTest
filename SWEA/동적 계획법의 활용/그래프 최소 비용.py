# 플로이드-워샬 알고리즘

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    DP = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i != j and DP[i][j] == 0:
                DP[i][j] = float('inf')

    for k in range(N):
        for i in range(N):
            if k == i:
                continue
            for j in range(N):
                if k == j or i == j:
                    continue
                DP[i][j] = min(DP[i][k] + DP[k][j], DP[i][j])

    print(f'#{test_case} {max(map(max, DP))}')
