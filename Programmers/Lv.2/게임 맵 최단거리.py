from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs(maps):
    r = len(maps)
    c = len(maps[0])

    deq = deque([(0, 0)])
    dist = [[-1 for _ in range(c)] for _ in range(r)]
    dist[0][0] = 1

    maps[r - 1][c - 1] = 2

    while deq:
        x, y = deq.popleft()
        if maps[x][y] == 2:
            return dist[x][y]

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]

            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                deq.append((nx, ny))

    return -1


def solution(maps):
    return bfs(maps)