from collections import deque
import copy

N, M, F = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(int, input().split()))
taxi[0]-=1
taxi[1]-=1

# 고객 정보를 담기 위한
customer_info=[[list() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    cx, cy, px, py=map(int, input().split()) # 고객 지점 cx, cy / 목표 지점 px, py
    customer_info[cx-1][cy-1]=[1, cx-1, cy-1, px-1, py-1] # 1은 출발지점
    customer_info[px-1][py-1]=[2, cx-1, cy-1, px-1, py-1] # 2는 도착지점

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def findCumtomer(): # bfs를 사용하여 고객 찾기
    x, y = taxi
    dist=0
    deq=deque([[x, y, dist]])
    visited = copy.deepcopy(board)
    visited[x][y]=-1

    # 가장 가까운 고객 지점 찾기
    result=[]
    while deq:
        x, y, dist= deq.popleft()
        print(x, y)
        dist+=1
        print(dist)
        if customer_info[x][y] and customer_info[x][y][0]==1:# 고객 출발 지점이라면
            result.append(customer_info[x][y])
            customer_info[x][y] = [] # 이미 택시 탄 고객은 좌표에서 초기화
            break
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<N and not board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=-1
                deq.append([nx, ny, dist])
                x, y = nx, ny

    return dist, result

def bringCustomer():

    return

for _ in range(M):
    dist, customer = findCumtomer()
    print(customer)
    print("dist:", dist)

print(F)