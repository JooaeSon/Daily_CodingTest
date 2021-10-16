from collections import defaultdict
from collections import deque


def bfs(wire, adj):
    deq = deque()

    while deq:
        n1 = deq.popleft()
        for n2 in adj[n1]:
            deq.append(n2)

    return


def solution(n, wires):
    answer = -1

    adj = defaultdict(list)

    for wire in wires:
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])

    print(adj)

    for wire in wires:
        bfs(wire, adj)

    return answer