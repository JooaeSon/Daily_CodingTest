from sys import stdin
import copy

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
answer = float('-inf')

def move(dir):
    # 해당 방향에서 다 끝으로 몰아넣기.

    if dir==0: # 왼쪽으로 몰아 넣음
        for i in range(N):
            idx=0
            for j in range(1, N):
                if board[i][j]: # 0이 아닐때
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][idx]==0:
                        board[i][idx]=temp
                    elif board[i][idx]==temp:
                        board[i][idx] = temp*2
                        idx+=1
                    else:
                        idx+=1
                        board[i][idx] = temp

    elif dir==1: # 오른쪽으로 몰아 넣음
        for i in range(N):
            idx=N-1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][idx]==0:
                        board[i][idx]=temp
                    elif board[i][idx]==temp:
                        board[i][idx] =temp*2
                        idx-=1
                    else:
                        idx-=1
                        board[i][idx] = temp

    elif dir==2: # 위쪽으로 몰아 넣음
        for j in range(N):
            idx=0
            for i in range(1, N):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if board[idx][j]==0:
                        board[idx][j]=temp
                    elif board[idx][j]==temp:
                        board[idx][j]=temp*2
                        idx+=1
                    else:
                        idx+=1
                        board[idx][j] = temp

    elif dir==3: # 아래 쪽으로 몰아 넣음
        for j in range(N):
            idx=N-1
            for i in range(N-2, -1, -1):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j] = 0
                    if board[idx][j]==0:
                        board[idx][j]=temp
                    elif board[idx][j]==temp:
                        board[idx][j]=temp*2
                        idx-=1
                    else:
                        idx-=1
                        board[idx][j] = temp


def dfs(cnt):
    global board, answer

    if cnt >= 5:
        if max(map(max, board)) > answer:
            answer = max(map(max, board))
        return

    tmp_board=copy.deepcopy(board) # 섞이기 전
    for i in range(4):
        move(i)
        dfs(cnt+1)
        board = copy.deepcopy(tmp_board)

# dfs 사용 :모든 가능성을 탐색 (상, 하, 좌, 우 번갈아 가면서 최대 5회 사용)
dfs(0)

print(answer)