# 우선순위 큐를 활용한 프림 알고리즘 사용

from heapq import *
from collections import defaultdict

T = int(input())

for test_case in range(1, T + 1):
    result = 0
    V, E = map(int, input().split())
    my_graph = defaultdict(list)
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        my_graph[n1].append((w, n2))
        my_graph[n2].append((w, n1))

    connected_node = set([0])
    cand_edge = my_graph[0]
    heapify(cand_edge)

    while cand_edge:
        weight, node = heappop(cand_edge) # 최소 우선순위 큐로 최소값 찾기
        if node not in connected_node:
            connected_node.add(node)
            result += weight #가중치 더해주기

            for edge in my_graph[node]: # node의 연결된 모든 node값들을 저장
                if edge[1] not in connected_node:
                    heappush(cand_edge, edge)

    print(f'#{test_case} {result}')
