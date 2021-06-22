import copy

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

infos = [list(map(int, input().split())) for _ in range(M)]
cloud = [[0 for _ in range(N)] for _ in range(N)]
cloud[N-1][0], cloud[N-1][1], cloud[N-2][0], cloud[N-2][1] = 1, 1, 1, 1

ans = 0

for info in infos:
    d, s = infos

    for i in range(N):
        for j in range(N):
            if cloud[i][j]==1:
                nx, ny = i+(s*dx[d])%N, j+(s*dy[d])%N


print(ans)