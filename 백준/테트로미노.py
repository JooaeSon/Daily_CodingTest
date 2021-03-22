import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tetromino = [[(0, 0), (0, 1), (1, 0), (1, 1)], # ㅁ
             [(0, 0), (0, 1), (0, 2), (0, 3)], # ㅡ
             [(0, 0), (1, 0), (2, 0), (3, 0)], #ㅣ
             [(0, 0), (0, 1), (1, 0), (2, 0)],
             [(0, 0), (0, 1), (0, 2), (1, 2)],
             [(0, 0), (0, 1), (0, 2), (1, 0)],
             [(0, 0), (0, 1), (1, 1), (2, 1)],
             [(0, 0), (1, 0), (2, 0), (2, 1)],
             [(1, 0), (1, 1), (1, 2), (0, 2)],
             [(0, 0), (1, 0), (1, 1), (1, 2)],
             [(2, 0), (0, 1), (1, 1), (2, 1)],
             [(0, 0), (0, 1), (0, 2), (1, 1)],
             [(0, 1), (1, 0), (1, 1), (1, 2)],
             [(1, 0), (0, 1), (1, 1), (2, 1)],
             [(0, 0), (1, 0), (2, 0), (1, 1)],
             [(0, 0), (1, 0), (1, 1), (2, 1)],
             [(0, 1), (0, 2), (1, 0), (1, 1)],
             [(0, 1), (1, 0), (1, 1), (2, 0)],
             [(0, 0), (0, 1), (1, 1), (1, 2)]]


def find(x, y):
    global answer

    for i in range(19):
        result=0
        for j in range(4):
            try:
                next_x=x+tetromino[i][j][0]
                next_y=y+tetromino[i][j][1]
                result+=board[next_x][next_y]
            except IndexError:
                continue
        answer = max(result, answer)


def solve():
    for i in range(N):
        for j in range(M):
            find(i, j)
    return


answer = 0
solve()
print(answer)

# 참고: https://jeongchul.tistory.com/670