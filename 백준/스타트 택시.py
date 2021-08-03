from collections import deque
import copy

N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

taxi = list(map(int, input().split()))
taxi[0]-=1
taxi[1]-=1

# 고객 정보를 담기 위한
customers=[list(map(int, input().split())) for _ in range(M)]
for cust in customers:
    board[cust[0]][cust[1]] = 2 # 손님의 춞발지점
    board[cust[0]][cust[1]] = 3 # 손님의 도착지점


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# 손님 찾기
def findCustomer(customer): # bfs를 사용하여 고객 찾기
    global F
    x, y = taxi
    dist=0

    deq=deque([(x, y, dist)])
    visited = copy.deepcopy(board)
    visited[x][y] = -1

    cx, cy, px, py = customer[0], customer[1], customer[2], customer[3]

    # 가장 가까운 고객 지점 찾기
    while deq:
        x, y, dist= deq.popleft()

        if cx==x and cy==y:
            F-=dist
            break

        for dir in range(4): # 상하좌우 탐색
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<N and not board[nx][ny] and not visited[nx][ny]: # 가는 길이 빈칸인지 아직 방문하지 않은 곳인지 확인
                visited[nx][ny]=-1
                deq.append((nx, ny, dist+1))
                x, y = nx, ny

    return


# 손님 데려다주기
def moveCustomer(customer):
    global F
    cx, cy, px, py = customer[0], customer[1], customer[2], customer[3]

    return

for _ in range(M):
    findCustomer(customers)
    moveCustomer(customers)

print(F)