def Dijkstra(G):
    D = [float('inf')] * (N+1)
    P = [None] * (N+1)
    visited = [False] * (N+1)

    D[0] = 0
    for _ in range(N):
        min_distance = float('inf')
        min_idx = -1

        # 최소 길이인 인덱스 찾기
        for i in range(N):
            if not visited[i] and min_distance > D[i]:
                min_distance = D[i]
                min_idx = i
        visited[min_idx] = True

        for e, w in G[min_idx]:
            if not visited[e] and D[min_idx] + w < D[e]:
                D[e] = D[min_idx] + w
                P[e] = min_idx
    return D[N]

T = int(input())

for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    G = {}
    for _ in range(E):
        # 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w
        s, e, w = map(int, input().split())
        if not s in G:
            G[s] = set()
        G[s].add((e, w))

    result = Dijkstra(G)
    print(f'#{test_case} {result}')
