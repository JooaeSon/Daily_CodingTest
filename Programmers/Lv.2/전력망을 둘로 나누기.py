from collections import defaultdict


def dfs(start, visited):
    global count

    visited.append(start)
    count += 1

    for vertax in adj[start]:
        if vertax not in visited:
            dfs(vertax, visited)

    return


def solution(n, wires):
    global count, adj
    result = []
    adj = defaultdict(list)

    for wire in wires:
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])

    for wire in wires:
        adj[wire[0]].remove(wire[1])
        adj[wire[1]].remove(wire[0])
        count = 0
        dfs(1, [])
        result.append(abs(n - 2 * count))  # 송전탑 개수의 차이의 최솟값 갱신
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])

    return min(result)