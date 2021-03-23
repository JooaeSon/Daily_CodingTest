import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def checkBoundary(x, y):
    return True if 0<=x<N and 0<=y<M else False

def clean(r, c, d):

    deq=deque([(r, c)])
    Map[r][c] = 2
    answer = 1

    while deq:
        x, y = deq.popleft()

        # 회전
        for i in range(4):
            nd=(d+3)%4
            nx, ny = x+dx[nd], y+dy[nd]
            d = nd
            if checkBoundary(nx, ny) and Map[nx][ny] == 0:
                deq.append((nx, ny))
                answer += 1
                Map[nx][ny]=2
                break

        else: # 네 방향 모두 청소가 되어 있거나 벽일때
            nd = (d+2)%4
            nx, ny = x + dx[nd], y + dy[nd]
            deq.append((nx, ny))

            # 뒷 칸도 벽인 경우
            if Map[nx][ny] == 1:
                return answer


print(clean(r, c, d))