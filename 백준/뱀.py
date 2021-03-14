from sys import stdin
from collections import deque

N = int(stdin.readline())
board = [[0]*N for _ in range(N)]

# 사과 위치 저장
K = int(stdin.readline())
for i in range(K):
    r, c = map(int, stdin.readline().split())
    board[r-1][c-1]=1
# 방향 정보 저장
D = int(stdin.readline())
dir_dic = {}
for _ in range(D):
    x, c = input().split()
    dir_dic[int(x)] = c

# 우, 하, 좌, 상
dy=[0, 1, 0, -1]
dx=[1, 0, -1, 0]

snake=deque([(0,0)])

def solution():
    time = 0
    pos_y, pos_x = 0, 0 # 해드 위치
    curr_dir=0

    while True:
        time += 1
        ny, nx = pos_y + dy[curr_dir], pos_x + dx[curr_dir]

        if 0<=ny<N and 0<=nx<N: # 범위 내에 움직일때만
            if (ny, nx) in snake: # 자기 자신에 부딪힌 경우
                break

            if board[ny][nx]==1: # 사과 있는 경우
                board[ny][nx] = 0
                snake.append((ny, nx))

            elif board[ny][nx]==0: # 사과가 없는 경우
                snake.append((ny, nx))
                snake.popleft()

            # 시간 체크
            if time in dir_dic:
                if dir_dic[time] == 'D':  # 오른쪽 회전
                    curr_dir = (curr_dir + 1) % 4
                else:  # 왼쪽 회전
                    curr_dir = (curr_dir - 1) % 4
            pos_y=ny
            pos_x=nx

        else:
            break

    return time

print(solution())
