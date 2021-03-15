import sys

input = sys.stdin.readline
N, M, x, y, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directs = list(map(int, input().split()))
dice = [0]*6 # 주사위 초기화

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.


for dir in directs:

    dir -= 1
    nx=x+dx[dir]
    ny=y+dy[dir]

    if 0 <= nx < N and 0 <= ny < M:

        # 주사위 회전
        if dir == 0:  # 동
            dice[0], dice[2], dice[3], dice[5]=dice[3], dice[0], dice[5], dice[2]
        elif dir == 1:  # 서
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif dir == 2:  # 북
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:  # 남
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0

        x, y = nx, ny
        print(dice[0]) # 주사위 값 출력

