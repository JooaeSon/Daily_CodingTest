def dfs(idx, visited):
    global Mini, S

    if idx > N - 1:
        if Mini >= sum(S):
            Mini = sum(S)
        return

    if Mini < sum(S):
        return

    for k in range(N):
        if visited[k] != 1:
            visited[k] = 1
            S.append(lst[idx][k])
            dfs(idx + 1, visited)
            visited[k] = 0
            S.pop()


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    Mini = 987654321
    S = []
    visited = [0] * N
    dfs(0, visited)

    print(f'#{test_case} {Mini}')