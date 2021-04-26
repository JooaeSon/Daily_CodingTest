N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 바람 방향에 따른 모래 비율
rate_left=[[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 'a', 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
rate_down=[[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 'a', 10, 0], [0, 0, 5, 0, 0]]
rate_right=[[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 'a', 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
rate_up=[[0, 0, 5, 0, 0], [0, 10, 'a', 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]


def spread(rate, nx, ny):
    global ans
    a, b = nx-2, ny-2

    temp=0
    for i in range(5):
        for j in range(5):
            if rate[i][j]!=0 and rate[i][j]!='a': # 숫자 비율 일때
                if 0 <= i+a < N and 0<= j+b <N:
                    A[i+a][j+b] += A[nx][ny]*rate[i][j]//100
                else:
                    # 범위에 들어오지 않을 경우
                    ans+=A[nx][ny]*rate[i][j]//100
                # a자리에 모래를 채워주기 위해 빠져나가는 모래 양을 temp에 계속 더해준다.
                temp+=A[nx][ny]*rate[i][j]//100
            # a 자리의 좌표를 기억    
            elif rate[i][j]=='a':
                remain = (i, j)
    
    # 나머지 a부분 처리
    if 0<=remain[0]+a<N and 0<=remain[1]+b<N:
        A[remain[0]+a][remain[1]+b] += A[nx][ny]-temp
    else: # a 자리도 격자 바깥일 경우 격자 바깥으로 나가는 ans에 더해준다.
        ans+=A[nx][ny]-temp

    # 0으로 초기화
    A[nx][ny]=0

    return


# 회오리 방향
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

# 초기 좌표
x, y = N//2, N//2
ans=0 # 격자 밖으로 나간 모래 양
dir, step = 0, 0
while True:

    if dir==0 or dir==2:
        step+=1

    if not 0<=x<N or not 0<=y<N:
        break

    cnt=0
    while cnt<step:
        nx, ny = x+dx[dir], y+dy[dir]

        if dir==0:
            spread(rate_left, nx, ny)
        elif dir==1:
            spread(rate_down, nx, ny)
        elif dir==2:
            spread(rate_right, nx, ny)
        else:
            spread(rate_up, nx, ny)

        cnt+=1
        x, y=nx, ny

    dir = (dir+1)%4


print(ans)
