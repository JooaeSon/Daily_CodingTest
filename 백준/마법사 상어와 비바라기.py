
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

infos = [list(map(int, input().split())) for _ in range(M)]
cloud = [[0 for _ in range(N)] for _ in range(N)]
cloud[N-1][0], cloud[N-1][1], cloud[N-2][0], cloud[N-2][1] = 1, 1, 1, 1

ans = 0

for info in infos:
    d, s = info
    d-=1
    tmp_cloud = [[0 for _ in range(N)] for _ in range(N)]

    # 모든 구름이 d 방향으로 s칸 이동한다.
    for i in range(N):
        for j in range(N):
            if cloud[i][j]==1:
                nx, ny = (i+s*dx[d])%N, (j+s*dy[d])%N
                tmp_cloud[nx][ny]=1

    cloud=tmp_cloud

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for i in range(N):
        for j in range(N):
            if cloud[i][j]==1:
                A[i][j]+=1

    # 대각선 계산
    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
    cross=[]
    for i in range(N):
        for j in range(N):
            if cloud[i][j]==1:
                cnt=0
                for k in (1, 3, 5, 7):
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if A[nx][ny]:
                            cnt+=1
                cross.append((i, j, cnt))

    for i, j, cnt in cross:
        A[i][j]+=cnt

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for i in range(N):
        for j in range(N):
            if cloud[i][j] != 1 and A[i][j]>=2:
                cloud[i][j] = 1
                A[i][j] -= 2
            else:
                cloud[i][j]=0

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
print(sum(map(sum, A)))