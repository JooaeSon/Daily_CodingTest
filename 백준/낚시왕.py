R, C, M = map(int, input().split())
sea=[[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sea[r-1][c-1]=(s, d, z)

# 위, 아래, 오른쪽, 왼쪽
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

answer=0

for time in range(C):
    # 땅과 제일 가까운 상어 잡기
    for k in range(R):
        if sea[k][time]: # 상어가 있다면
            answer += sea[k][time][2]# 잡은 상어 크기 추가
            sea[k][time]=0
            break
    # 상어가 이동
    tmp_sea=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if sea[i][j]:
                s, d, z = sea[i][j]
                x, y = i, j
                move=s
                while move:
                    nx, ny = x+dx[d-1], y+dy[d-1]
                    if not 0<=nx<R or not 0<=ny<C:
                        if d==1: d=2
                        elif d==2: d=1
                        elif d==3: d=4
                        elif d==4: d=3
                        nx, ny = x+dx[d-1], y+dy[d-1]
                    x, y = nx, ny
                    move-=1
                if tmp_sea[x][y]: #이미 다른 상어가 있다면
                    if tmp_sea[x][y][2]<z: # 사이즈 큰애가 먹는다.
                        tmp_sea[x][y]=(s, d, z)
                else:
                    tmp_sea[x][y]=(s, d, z)
    sea = tmp_sea

print(answer)