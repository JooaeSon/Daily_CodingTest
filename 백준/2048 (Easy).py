from sys import stdin

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move(nx, ny):
    # 해당 방향에서 다 끝으로 몰아넣기.

    if nx==-1: # 왼쪽으로 몰아 넣음
        for i in range(N):
            idx=0
            for j in range(1, N):
                if board[i][j]: # 0이 아닐때
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][idx]==0:
                        board[i][idx]=temp
                    elif board[i][idx]==temp:
                        board[i][idx] *= 2
                        idx+=1
                    else:
                        idx+=1
                        board[i][idx] = temp

    elif nx==1: # 오른쪽으로 몰아 넣음

    elif ny==-1: # 위쪽으로 몰아 넣음

    elif ny == 1: # 아래 쪽으로 몰아 넣음


    return


def dfs(cnt):
    if cnt >= 5:
        print(max(map(max, board)))
        return

    move(dx[dir], dy[dir])

    for i in range(4):
        dfs(cnt+1)


def solution():
    # dfs 사용 :모든 가능성을 탐색 (상, 하, 좌, 우 번갈아 가면서 최대 5회 사용)
    if N == 1:
        print(board[0][0])
        return

    dfs(0)

    return

solution()