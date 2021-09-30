from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):

    deq = deque([(x, y)])
    cnt=0
    while deq:
        x, y=deq.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<N:
                deq.append((nx, ny))
                cnt+=1
    return


for i in range(N):
    for j in range(N):
        bfs(i, j)
print(ans)