
r, c, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]
# t초 동안 방에 남아 있는 미세먼지 양 구하기

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 공기 청정기 좌표 찾기
airclean=[]

for i in range(r):
    for j in range(c):
        if A[i][j]==-1:
            airclean.append((i, j))


def diffuse(x, y):
    cnt=0 # 확산된 방향 개수 세주기
    moveAmount=A[x][y]//5 # 확산되는 양

    for dir in range(4):
        nx, ny = x+dx[dir], y+dy[dir]
        if 0<=nx<r and 0<=ny<c and A[nx][ny]!=-1:
            cnt+=1
            tmp_A[nx][ny]+=moveAmount

    tmp_A[x][y]+=A[x][y]-(A[x][y]//5)*cnt


def cleaning(first_clean, second_clean):
    fx, fy = first_clean[0], first_clean[1]
    sx, sy = second_clean[0], second_clean[1]
    
    # 반시계 방향
    post = 0
    for dxx, dyy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        while True:
            nfx, nfy = fx + dxx, fy + dyy
            if not 0<=nfx<r or not 0<=nfy<c:
                break
            if A[nfx][nfy]==-1:
                break
            tmp= A[nfx][nfy]
            A[nfx][nfy] = post
            post=tmp

            fx, fy = nfx, nfy

    # 시계 방향
    post = 0
    for dxx, dyy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        while True:
            nsx, nsy = sx + dxx, sy + dyy
            if not 0 <= nsx < r or not 0 <= nsy < c:
                break
            if A[nsx][nsy] == -1:
                break
            tmp = A[nsx][nsy]
            A[nsx][nsy] = post
            post = tmp

            sx, sy = nsx, nsy

    return


for _ in range(t): # t 초 동안 값 구하기
    # 미세 먼지 확산하기
    tmp_A=[[0]*c for _ in range(r)]
    tmp_A[airclean[0][0]][airclean[0][1]]=-1
    tmp_A[airclean[1][0]][airclean[1][1]] = -1
    for i in range(r):
        for j in range(c):
            if A[i][j] != 0 and A[i][j] != -1:
                diffuse(i, j)

    A = tmp_A

    # 공기 청정기 작동
    airclean.sort()
    first_clean=airclean[0] # 반시계 방향
    second_clean=airclean[1] # 시계 방향

    cleaning(first_clean, second_clean)

answer=0

for i in range(r):
    for j in range(c):
        if A[i][j]!=-1:
            answer+=A[i][j]
print(answer)