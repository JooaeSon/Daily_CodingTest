import sys
# 런타임 에러를 방지하기 위한 재귀호출 제한(1000번 이상으로 할 때)
sys.setrecursionlimit(10**5)

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]


for l in L:
    size=2**l
    
    # 회전
    for x in range(0, len(A), size):
        for y in range(0, len(A), size):
            temp=[A[i][y:y+size] for i in range(x, x+size)]

            for i in range(size):
                for j in range(size):
                    A[x+j][y+size-1-i]=temp[i][j]

    # 인접 얼음 3개 미만인 것 찾기
    three_down=[]
    for x in range(len(A)):
        for y in range(len(A)):
            cnt=0
            for dir in range(4):
                nx, ny = x+dx[dir], y+dy[dir]
                if 0<=nx<len(A) and 0<=ny<len(A) and A[nx][ny]:
                    cnt+=1
            if cnt<3:
                three_down.append((x, y))
    
    # 얼음 제거하기 -1
    for i in range(len(three_down)):
        x, y = three_down[i]
        if A[x][y] > 0:
            A[x][y]-=1

print(sum(map(sum, A))) #남아 있는 얼음의 합 구하기


def dfs(x, y):
    global Sum

    A[x][y] = 0  # 이미 방문한 곳은 표시
    Sum+=1

    for dir in range(4):
        nx, ny = x+dx[dir], y+dy[dir]
        if 0<=nx<len(A) and 0<=ny<len(A) and A[nx][ny]:
            dfs(nx, ny)

ans=0
for i in range(len(A)):
    for j in range(len(A)):
        Sum = 0
        if A[i][j]:
            dfs(i, j)
            ans=max(Sum, ans)
    
print(ans)

