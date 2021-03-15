from sys import stdin
N = int(stdin.readline())
T, P = [0]*N, [0]*N

for i in range(N):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

dp = [0]*(N+1)


def solution():

    for i in range(N):
        if dp[i] > dp[i+1]: # 앞의 일정 최댓값이 더 크다면 현재 값을 앞의 값으로 갱신
            dp[i+1] = dp[i]

        if i+T[i] <= N:
            # 미래 날짜 축적되어 있는 최대 값 vs 현재 최대 축적 값+상담했을때 미래에 받을 수 있는 값
            dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])

    return dp[N]


print(solution())

