N = int(input())
curves = [tuple(map(int, input().split())) for _ in range(N)]
board=[[0]*101 for _ in range(101)]
dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]
dragon=[]

ans=0
end_x, end_y = 0, 0

def make_generation():
    global end_x, end_y

    size = len(dragon)
    for idx in range(size-1, -1, -1): # 바로 전 세대 만큼 횟수를 반복하여 현재세대에는 어떠한 방향으로 바뀌었는지 확인하고 체크 및 append

        dir=(dragon[idx]+1)%4

        end_x=end_x+dx[dir]
        end_y=end_y+dy[dir]

        board[end_y][end_x]=-1
        dragon.append(dir)

    return

for curve in curves:
    x, y, d, g = curve[0], curve[1], curve[2], curve[3]

    dragon.clear()

    end_x, end_y=x, y
    board[end_y][end_x]= -1

    end_x, end_y = x+dx[d], y+dy[d]
    board[end_y][end_x] = -1

    dragon.append(d)
    
    # 세대별로 생성하기
    for i in range(g):
        make_generation()

for i in range(100):
    for j in range(100):
        if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]==-1:
            ans+=1

print(ans)

