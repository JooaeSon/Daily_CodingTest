T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, M = map(int, input().split())

    weight = [0]
    value = [0]
    for _ in range(M):
        size, price = map(int, input().split())
        weight.append(size)
        value.append(price)

    # 상향식 동적계획법으로 쌓아간다.
    K = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1): # 물건 인덱스를 가르키는 i
        for w in range(1, N + 1): # 1부터 N까지 늘어나는 가방 무게
            if w < weight[i]:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w - weight[i]] + value[i], K[i - 1][w])

    print(f'#{test_case} {K[M][N]}')
