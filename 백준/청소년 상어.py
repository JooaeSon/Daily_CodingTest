from copy import deepcopy

sea=[[] for _ in range(4)]
# 상어와 물고기의 위치 담을 곳
pos = [[] for _ in range(16)]

for i in range(4):
    row=list(map(int, input().split()))
    for j in range(0, 7, 2):
        sea[i].append([row[j]-1, row[j+1]-1])
        pos[row[j]-1]=[i, j//2]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(x, y, d, cnt):
    global ans, sea, pos
    move_fish(x, y)

    while True:
        nx, ny = x+dx[d], y+dy[d] # 방향에 있는 칸으로 이동하기 위함
        if not 0<=nx<4 or not 0<=ny<4: # 상어가 더 이상 이동할 수 있는 칸이 없다면
            ans = max(ans, cnt)
            return
        if not sea[nx][ny]: # 물고기가 없는 칸으로는 이동할 수 x
            x, y = nx, ny # 재귀호출 생략하고 바로 다음 좌표로 갱신
            continue

        temp_sea, temp_pos = deepcopy(sea), deepcopy(pos)
        temp1, temp2 = pos[sea[nx][ny][0]], sea[nx][ny]
        pos[sea[nx][ny][0]], sea[nx][ny] = [], []
        dfs(nx, ny, temp2[1], cnt+temp2[0]+1) # 상어 이동
        sea, pos = temp_sea, temp_pos
        # pos[sea[nx][ny][0]], sea[nx][ny] = temp1, temp2
        x, y = nx, ny


def move_fish(sx, sy):
    # 물고기 이동
    for i in range(len(pos)):
        if pos[i]:
            x, y = pos[i][0], pos[i][1]
            rotate=0
            while True:
                if rotate==8: # 한바퀴 다 돌았으면 더이상 x
                    break
                nx, ny = x+dx[sea[x][y][1]], y+dy[sea[x][y][1]]

                if 0<=nx<4 and 0<=ny<4 and not (nx==sx and ny==sy):
                    if sea[nx][ny]: # 물고기가 있을 때만
                        pos[sea[nx][ny][0]] = [x, y]
                    sea[x][y], sea[nx][ny]=sea[nx][ny], sea[x][y]
                    pos[i]=[nx, ny]
                    break
                else: # 이동할 수 있는 칸이 있을 때까지 45'반시계
                    sea[x][y][1]=(sea[x][y][1]+1)%8
                    rotate+=1


ans=0
d, cnt = sea[0][0][1], sea[0][0][0]+1
pos[sea[0][0][0]], sea[0][0] = [], []
dfs(0, 0, d, cnt)
print(ans)


