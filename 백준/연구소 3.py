from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab=[list(map(int, input().split())) for _ in range(N)]

# 바이러스 놓을 수 있는 위치 찾기
virus_able=[]
for i in range(N):
    for j in range(N):
        if lab[i][j]==2:
            virus_able.append((i, j))

# 바이러스 M개 위치 경우의 수 조합 만들기
virus_combis=list(combinations(virus_able, M))

dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]

def bfs(v_list):
    dist=[[-1]* N for _ in range(N)]
    deq=deque()
    for pos in v_list:
        deq.append(pos)
        dist[pos[0]][pos[1]]=0
    max_dist=0
    while deq:
        x, y = deq.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<N and lab[nx][ny]!=1 and dist[nx][ny]==-1 :
                dist[nx][ny] = dist[x][y]+1
                if lab[nx][ny]==0:
                    max_dist=max(max_dist, dist[nx][ny])
                deq.append((nx, ny))

    # 방문 안한 곳이 벽 개수와 동일한지
    if list(sum(dist, [])).count(-1)==list(sum(lab, [])).count(1):
        ans.append(max_dist)


ans=[]
# 바이러스 경우의 수를 하나씩 고려하기
for v in virus_combis:
    bfs(v)

print(min(ans) if ans else -1)