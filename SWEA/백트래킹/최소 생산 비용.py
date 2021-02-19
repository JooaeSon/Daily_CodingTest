def dfs(product_num):
    global result, Sum

    if product_num >= N:
        if Sum <= result:
            result = Sum
        return

    if Sum >= result:
        return

    for factory in range(N):
        if visited[factory] != -1:
            visited[factory] = -1
            Sum += V[product_num][factory]
            dfs(product_num + 1)
            visited[factory] = 0
            Sum -= V[product_num][factory]


T = int(input())

for test_case in range(1, T + 1):
    result, Sum = float('inf'), 0
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    dfs(0)

    print(f'#{test_case} {result}')
