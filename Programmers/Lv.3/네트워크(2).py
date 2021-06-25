def dfs(cnum, visited, computers):
    for i in range(len(computers[cnum])):
        if computers[cnum][i] and not visited[i]:
            visited[i] = 1
            dfs(i, visited, computers)


def solution(n, computers):
    cnt = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i, visited, computers)

    return cnt