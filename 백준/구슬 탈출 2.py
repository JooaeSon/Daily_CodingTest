from sys import stdin
from collections import deque

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


def movemove(x, y, ddx, ddy):
    move = 0

    while board[x + ddx][y + ddy] != '#':
        if board[x+ddx][y+ddy] == 'O': # 구멍으로 탈출 할 경우
            return 0, 0, 0
        x += ddx
        y += ddy
        move += 1

    return x, y, move


def BFS():
    visit = {}
    deq = deque([red+blue])
    visit[red[0], red[1], blue[0], blue[1]] = 0

    while deq:
        rx, ry, bx, by = deq.popleft()

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            # 한쪽 방향으로 계속 움직일 수 있을 때까지 움직인다.
            nrx, nry, rmove = movemove(rx, ry, dx, dy)
            nbx, nby, bmove = movemove(bx, by, dx, dy)

            # 두 공 모두 또는 파란 공만 탈출한 경우
            if not nbx and not nby:
                continue
            # 빨간 공만 탈출한 경우
            elif not nrx and not nry:
                print(visit[rx, ry, bx, by]+1)
                return
            # 두 공이 같은 위치에 있는 경우
            elif nrx == nbx and nry == nby:
                # 이동 거리가 많은 구슬을 한 칸 뒤로
                if rmove > bmove:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            # visit하지 않았으면 queue에 append
            if (nrx, nry, nbx, nby) not in visit:
                visit[nrx, nry, nbx, nby] = visit[rx, ry, bx, by]+1
                deq.append([nrx, nry, nbx, nby])

        # answer에 값을 넣었거나 deq이 비었거나 움직인 횟수가 10 이상일때
        if not deq or visit[rx, ry, bx, by] >= 10:
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