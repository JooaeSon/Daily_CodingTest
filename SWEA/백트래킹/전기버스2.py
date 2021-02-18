def dfs(idx):
    global result, cnt

    if idx >= N:
        if cnt <= result:
            result = cnt
        return

    if result <= cnt:
        return

    for i in range(1, M[idx] + 1):
        cnt += 1
        dfs(idx + i)
        cnt -= 1


T = int(input())

for test_case in range(1, T + 1):
    result, cnt = 987654321, -1
    lst = list(map(int, input().split()))
    N = lst[0] - 1
    M = lst[1:]

    dfs(0)

    print(f'#{test_case} {result}')
