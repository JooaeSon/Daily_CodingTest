N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 회오리 방향
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

x, y = N//2, N//2
ans=0
dir, step = 0, 0
while True:

    if dir==0 or dir==2:
        step+=1

    if not 0<=x<N or not 0<=y<N:
        break

    cnt=0
    while cnt<step:
        nx, ny = x+dx[dir], y+dy[dir]
        print(nx, ny)
        cnt+=1
        x, y=nx, ny



    dir = (dir+1)%4




print(ans)
