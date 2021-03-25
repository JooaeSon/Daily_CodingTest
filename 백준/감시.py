from collections import deque
import copy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

# 남, 서, 북, 동
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# cctv 설치 된 좌표 찾기
cctv = []
for i in range(N):
    for j in range(M):
        if office[i][j] in (1, 2, 3, 4, 5):
            cctv.append((i, j))

def dfs(cnt):
    global answer, tmp_office

    if cnt >= len(cctv):
        tmp_office=copy.deepcopy(office)
        c=0
        for i in range(len(cctv)):
            x, y = cctv[i]
            if office[x][y]==1:
                c+=move(x, y, dir[i])
            elif office[x][y]==2:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i]+2)%4)
            elif office[x][y]==3:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i]+1)%4)
            elif office[x][y]==4:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
                c += move(x, y, (dir[i] + 2) % 4)
            else:
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
                c += move(x, y, (dir[i] + 2) % 4)
                c += move(x, y, (dir[i] + 3) % 4)

        answer = min(answer, N*M-c)
        return

    for i in range(4): # 방향의 경우의 수 생각
        dir.append(i)
        dfs(cnt+1)
        dir.pop()

def move(x, y, d):
    cnt = 0
    while True:
        nx, ny= x+dx[d], y+dy[d]
        if not 0<=nx<N or not 0<=ny<M or tmp_office[nx][ny]==6:
            return cnt
        if 0 < tmp_office[nx][ny] < 6 or tmp_office[nx][ny]==-1: # 또다른 카메라가 설치되었거나 이미 지나갔던 길이라면 과정 생략 가능
            x, y = nx, ny
            continue

        tmp_office[nx][ny]=-1
        cnt+=1
        x, y=nx, ny
    return
answer = float('inf')
dir = deque()
dfs(0)

#카메라 및 벽의 갯수 확인하기
cnt=0
for i in range(N):
    for j in range(M):
        if office[i][j] in (1, 2, 3, 4, 5, 6):
            cnt+=1

print(answer-cnt)

# PyPy3로 돌려야 가능