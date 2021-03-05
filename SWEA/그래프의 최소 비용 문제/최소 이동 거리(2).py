from collections import *
from heapq import *

# 우선순위 큐 활용
def dijkstra(start):
    connected_node = set()
    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    heap = []
    heappush(heap, (dist[start], start))
    while heap:
        curr_dist, curr_node = heappop(heap)

        if curr_node not in connected_node:
            connected_node.add(curr_node)

            for e in my_graph[curr_node]:
                if e[0] not in connected_node and curr_dist + e[1] < dist[e[0]]:
                    dist[e[0]] = curr_dist + e[1]
                    heappush(heap, (dist[e[0]], e[0]))

    return dist


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, E = map(int, input().split())

    my_graph = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        my_graph[s].append((e, w))

    result = dijkstra(0)

    print(f'#{test_case} {result[N]}')
