from collections import deque

N, L, R = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(i, j):
    global change
    # 하나의 연합 생성
    deq = deque([(i, j)])
    routes = [(i, j)]

    cnt, Sum=0, 0
    while deq:
        x, y = deq.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if not 0<=nx<N or not 0<=ny<N:
                continue
            if not visited[nx][ny] and L<=abs(A[x][y]-A[nx][ny])<=R:
                cnt+=1
                Sum+=A[nx][ny]
                visited[nx][ny]=1
                routes.append((nx, ny))
                deq.append((nx, ny))
    if cnt > 0:
        population = Sum//cnt
        change+=1
        for x, y in routes:
            A[x][y]=population

    return


ans=0
while True:
    visited = [[0] * N for _ in range(N)]
    change = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]: # 아직 방문이 되지 않은 국가만 기준으로 bfs
                bfs(i, j)
    if change==0: # 더이상 변화가 없다면
        break
    ans+=1

print(ans)