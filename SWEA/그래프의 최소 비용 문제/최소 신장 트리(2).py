from collections import defaultdict
from heapq import *


def Prim():
    global result

    connected_node = set([0])
    heap = dic[0]
    heapify(heap)

    while heap:
        weight, node = heappop(heap)  # 최소 가중치 pop()
        if node not in connected_node:
            connected_node.add(node)
            result += weight

            for e in dic[node]:
                if e not in connected_node:
                    heappush(heap, e)

    return


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    V, E = map(int, input().split())
    dic = defaultdict(list)

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        dic[n1].append((w, n2))
        dic[n2].append((w, n1))

    Prim()

    print(f'#{test_case} {result}')
