from sys import stdin
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N, M = map(int, stdin.readline().split())
board = [list(stdin.readline()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue = [i, j]
            board[i][j] = '.'


def movemove(y, x, ddy, ddx):
    move = 0

    while board[y + ddy][x + ddx] != '#':
        if board[y+ddy][x+ddx] == 'O': # 구멍으로 탈출 할 경우
            return 0, 0, 0
        y += ddy
        x += ddx
        move += 1

    return y, x, move


def BFS():
    visit = {}
    deq = deque([red+blue])
    visit[red[0], red[1], blue[0], blue[1]] = 0

    while deq:
        ry, rx, by, bx = deq.popleft()

        for k in range(4):
            # 한쪽 방향으로 계속 움직일 수 있을 때까지 움직인다.
            nry, nrx, rmove = movemove(ry, rx, dy[k], dx[k])
            nby, nbx, bmove = movemove(by, bx, dy[k], dx[k])

            # 두 공 모두 또는 파란 공만 탈출한 경우
            if not nbx and not nby:
                continue
            # 빨간 공만 탈출한 경우
            elif not nrx and not nry:
                print(visit[ry, rx, by, bx]+1)
                return
            # 두 공이 같은 위치에 있는 경우
            elif nrx == nbx and nry==nby:
                # 이동거리가 적은 구슬을 한 칸 뒤로
                if rmove > bmove:
                    nrx -= dx[k]
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]
            # visit하지 않았으면 queue에 append
            if (nry, nrx, nby, nbx) not in visit:
                visit[nry, nrx, nby, nbx] = visit[ry, rx, by, bx]+1
                deq.append([nry, nrx, nby, nbx])

    # answer에 값을 넣었거나 deq이 비었거나 움직인 횟수가 10 이상일때
    if not deq or visit[ry, rx, by, bx] >= 10:
        print(-1)
        return

BFS()

'''
5 5
#####
#..B#
#.#.#
#RO.#
#####

'''

# 참고: https://seoyoung2.github.io/algorithm/2020/06/18/Baekjoon-13460.html