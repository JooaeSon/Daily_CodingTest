from collections import deque

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

deq=deque()
# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if A[i][j]==9:
            deq.append((i, j, 0))
            A[i][j] = 0
            break

babySize=2
def bfs():
    global babySize

    eaten = []
    c = [[-1]*N for _ in range(N)]
    while deq:
        x, y, dist= deq.popleft()


        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and A[nx][ny] != -1 and A[nx][ny]<=babySize: # 아기 상어가 움직일 수 있는 조건
                if A[nx][ny] != 0 and A[nx][ny]<babySize: # 물고기가 있는 곳이고 아기 상어보다 작은 물고기
                        eaten.append((nx, ny)) # 먹은 물고기 위치 넣기
                deq.append((nx, ny, dist+1))
                A[nx][ny] = -1


    return


bfs()

print(time)