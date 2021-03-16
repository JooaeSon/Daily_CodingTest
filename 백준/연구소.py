from sys import stdin
import itertools
from collections import deque
import copy
# 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

N, M = map(int, stdin.readline().split())
Lab = [list(map(int, stdin.readline().split())) for _ in range(N)]
com=[] # 조합 생성
for i in range(N):
    for j in range(M):
        if Lab[i][j]==0:
            com.append((i, j))


def bfs(y, x):
    # 바이러스는 상하좌우로만 이동 가능
    deq=deque([(y, x)])
    while deq:
        y, x = deq.popleft()
        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<M and temp_Lab[ny][nx]!=1 and visited[ny][nx]==0:
                visited[ny][nx] = -1
                temp_Lab[ny][nx]=2 # 전염
                deq.append((ny, nx))

    return

# 벽 3개를 세울 수 있는 모든 조합을 고려한다.
walls = list(itertools.combinations(com, 3))
answer=0
for wall in walls: # 조합을 하나씩 꺼내서 바이러스가 최대한 안퍼지는 경우를 고려한다.
    temp_Lab=copy.deepcopy(Lab)
    secure = 0
    for i in range(len(wall)):
        y, x = wall[i]
        temp_Lab[y][x] = 1 # 해당 벽 세우기
    # 3개의 벽을 다 세우고 난 다음 bfs를 사용하여 바이러스 퍼뜨리기
    visited=[[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if temp_Lab[i][j]==2: # 바이러스가 있는 곳을 중심으로
                bfs(i, j) # 확산 시작

    for l in temp_Lab: # 안전 지대 개수는?
        secure+=l.count(0)

    # 안전 지역 최대 값 갱신
    if secure > answer:
        answer = secure

print(answer)