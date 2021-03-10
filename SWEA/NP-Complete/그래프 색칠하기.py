from collections import defaultdict


def COLORING():
    colors = set([i for i in range(1, M+1)]) # 사용 할 수 있는 색깔

    for adjV in adjacent:
        colors -= colored[adjV]

    if not colors:
       return False

    colored[node] = {min(colors)}

    return True


T = int(input())

for test_case in range(1, T + 1):
    result = 1

    N, E, M = map(int, input().split())

    colored = [{0}]*(N+1) # 각 노드 마다 색칠 되어있는 색깔 알기 위해
    graph = defaultdict(set)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].add(v2)
        graph[v2].add(v1)

    for node in graph:
        adjacent = graph[node] # 인접한 점들 확인
        if not COLORING():
            result = 0
            break

    print(f'#{test_case} {result}')