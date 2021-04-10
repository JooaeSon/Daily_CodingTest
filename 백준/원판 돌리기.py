import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    deq.append([x, y])
    xcnt=0
    while deq:
        x, y =deq.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if ny < 0:
                ny = M-1
            elif ny > M-1:
                ny = 0

            if 0<=nx<N and 0<=ny<M and not c[nx][ny]:
                if Round[x][y]==Round[nx][ny]:
                    c[nx][ny]=1
                    deq.append([nx, ny])
                    xcnt+=1
    return xcnt


N, M, T = map(int, input().split())

Round, nsum, nm = [], 0, N*M
for _ in range(N):
    row = list(map(int, input().split()))
    Round.append(row)
    nsum+=sum(row)

deq = deque()
c = [[0]*M for _ in range(N)]

for _ in range(T):
    # x배수, d방향, k칸 회전
    x, d, k = map(int, input().split())

    k %= M
    for i in range(x-1, N, x):
        if d==0: # 시계
            Round[i] = Round[i][-k:]+Round[i][:-k]
            c[i] = c[i][-k:] + c[i][:-k]
        else: # 반시계
            Round[i] = Round[i][k:] + Round[i][:k]
            c[i] = c[i][k:] + c[i][:k]

    flag = 0
    for i in range(N):
        for j in range(M):
            if not c[i][j]:
                cnt=bfs(i, j)
                if cnt:
                    nsum -= Round[i][j]*cnt
                    nm-=cnt
                    flag=1
    if nm==0:
        print(0)
        sys.exit()

    if not flag: # 하나도 일치하는 수가 없었을 경우
        avg = nsum/nm
        for i in range(N):
            for j in range(M): 
                if not c[i][j]: # 아직 남아있는 숫자들 한에서
                    if Round[i][j]>avg:
                        Round[i][j] -= 1
                        nsum -=1
                    elif Round[i][j]< avg:
                        Round[i][j] +=1
                        nsum+=1

print(nsum)

# 참고: https://chldkato.tistory.com/132