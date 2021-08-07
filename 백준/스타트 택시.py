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
    board[cust[0]-1][cust[1]-1] = 2 # 손님의 춞발지점
print(board)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 손님 찾기
def findCustomer(taxi): # bfs를 사용하여 고객 찾기
    global F
    x, y = taxi
    dist=0

    deq=deque([(x, y, dist)])
    visited = copy.deepcopy(board)
    visited[x][y] = -1

    # 가장 가까운 고객 지점 찾기
    while deq:
        x, y, dist = deq.popleft()

        if board[x][y] == 2:
            board[x][y]=0
            break

        for dir in range(4): # 상하좌우 탐색
            nx, ny = x+dx[dir], y+dy[dir]

            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 1 and visited[nx][ny]!=-1: # 가는 길이 빈칸인지 아직 방문하지 않은 곳인지 확인
                visited[nx][ny]=-1
                dist+=1
                deq.append((nx, ny, dist))
                x, y = nx, ny

    taxi[0], taxi[1] = x, y
    print("###", x, y)
    return dist, taxi


# 손님 데려다주기
def moveCustomer(taxi):
    global F
    x, y = taxi

    fx, fy = 0, 0
    for cust in customers:
        if cust[0]-1 == x and cust[1]-1 == y:
            fx, fy = cust[2]-1, cust[3]-1
            break
    dist=0
    deq = deque([(x, y, dist)])
    visited = copy.deepcopy(board)
    visited[x][y]=-1

    while deq:
        x, y, dist=deq.popleft()

        if fx==x and fy==y:
            break

        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<N and board[nx][ny]!=1 and visited[nx][ny] !=-1:
                visited[nx][ny]=-1
                dist+=1
                deq.append((nx, ny, dist))
                x, y = nx, ny
    print("*****", x, y)
    taxi[0], taxi[1] = x, y
    print(taxi, "*********************************************")
    return dist, taxi


for _ in range(M):
    dist, taxi=findCustomer(taxi)
    print("1:", dist, taxi)
    dist, taxi=moveCustomer(taxi)
    print("2:", dist, taxi)
print(F)