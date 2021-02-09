def solution(m, n, puddles):
    road = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for j in range(n + 1):
        for i in range(m + 1):
            if j == 1 and i == 1:
                road[j][i] = 1
                continue

            if [i, j] in puddles:
                road[j][i] == 0
            else:
                road[j][i] += road[j - 1][i] + road[j][i - 1]

    return road[n][m] % 1000000007