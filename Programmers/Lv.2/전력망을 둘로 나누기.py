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

# 참조: https://velog.io/@corone_hi/314.-%EC%A0%84%EB%A0%A5%EB%A7%9D%EC%9D%84-%EB%91%98%EB%A1%9C-%EB%82%98%EB%88%84%EA%B8%B0