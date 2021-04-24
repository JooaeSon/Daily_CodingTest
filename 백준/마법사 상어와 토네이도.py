N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 회오리 방향
dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

x, y = N//2, N//2
ans=0
while True:

    if x==0 and y==0:
        break



print(ans)
