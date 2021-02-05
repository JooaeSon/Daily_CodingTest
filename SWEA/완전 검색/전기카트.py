def dfs(start, end):
    global result, Sum

    if 0 not in visited:
        if result > Sum + lst[end][0]:  # 사무실에 도착 했을때, 최소 값 구하기
            result = Sum + lst[end][0]
        return

    for i in range(N):
        if i != 0 and i != end and visited[i] != 1:  # 자기 자신이 아니고 아직 방문 안했을 경우(사무실 도착 이전 시)
            Sum += lst[end][i]
            visited[i] = 1
            dfs(end, i)
            Sum -= lst[end][i]
            visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    result = float('inf')
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    visited[0] = 1
    Sum = lst[0][0]
    dfs(0, 0)

    print(f'#{test_case} {result}')
