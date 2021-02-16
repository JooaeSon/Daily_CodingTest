def dfs(n, computers, visited, CNUM):
    for j in range(len(computers[CNUM])):
        if j != CNUM and computers[CNUM][j] == 1 and visited[j] != -1:
            visited[j] = -1
            dfs(n, computers, visited, j)


def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(len(computers)):
        if visited[i] == 0:
            answer += 1
            dfs(n, computers, visited, i)

    return answer