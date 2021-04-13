N = int(input())
red_blue=[[0 for _ in range(10)] for _ in range(4)]
red_green=[[0 for _ in range(4)] for _ in range(10)]

for _ in range(N):
    t, x, y = map(int, input().split())
    if t==1: # 크기가 1×1인 블록을 (x, y)에 놓은 경우
        red_blue[x][y]=1
    elif t==2: # 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
        red_blue[x][y]=1
        red_blue[x][y+1]=1
    else: # 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
        red_blue[x][y]=1
        red_blue[x+1][y]=1
