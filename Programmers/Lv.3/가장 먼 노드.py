from collections import *


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)

    adj = defaultdict(list)

    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    deq = deque([(1, 0)])
    while deq:
        node, cnt = deq.popleft()

        if visited[node] == -1:
            visited[node] = cnt
            for n in adj[node]:
                deq.append((n, cnt + 1))

    for v in visited:
        if v == max(visited):
            answer += 1

    return answer