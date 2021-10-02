from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

area=[]

def isInGroup(): # 격자에 그룹이 존재하는지 확인

    return True

def bfs(x, y):

    deq = deque([(x, y)])
    cnt=0
    while deq:
        x, y=deq.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and board[nx][ny]!=-1:
                deq.append((nx, ny))
                visited[nx][ny] = -1
                cnt+=1
    return


while True:
    if not isInGroup():
        break

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j]!=-1:
                bfs(i, j)

print(ans)