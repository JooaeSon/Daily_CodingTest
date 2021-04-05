from collections import deque
import heapq

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if A[i][j]==9:
            start=(i, j, 0)
            break


def find_min_dist(start, curr_size): # 최소 물고기 거리 값 찾기
    deq = deque()
    deq.append(start)

    x, y, cnt = start
    # 시작 값을 0으로 변경
    A[x][y]=0

    visited=set()
    # min_dist는 heapq구조. (cnt, x, y) 형태로 저장(갯수->제일 위의 좌표->제일 왼쪽 순으로 정렬)
    min_dist=[]
    while deq:
        x, y, cnt = deq.popleft()
        visited.add((x, y))
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and (nx, ny) not in visited:
                visited.add((nx, ny))

                # 다음 칸으로 이동할 수 있는 경우
                if A[nx][ny]==0 or A[nx][ny]==curr_size:
                    deq.append((nx, ny, cnt+1))
                    continue

                # 지나 갈 수 없는 경우
                if A[nx][ny] > curr_size:
                    continue
                else:
                    # 먹을 수 있는 경우
                    heapq.heappush(min_dist, (cnt+1, nx, ny))

    # 먹을 수 있는 후보군에 적합한 조건인 것
    if min_dist:
        return min_dist[0]
    else:
        return None

time=0
already_eat=0
curr_size=2
while True:
    next_val = find_min_dist(start, curr_size)

    if next_val is None:
        break

    # cnt = 다음 물고기를 먹기까지 걸린 시간
    cnt, nx, ny = next_val
    time+=cnt

    # 먹은 물고기 개수를 센다.
    already_eat+=1
    
    # 현재 크기만큼 먹었으면 현재 크기의 +1 하고 이미 먹어왔던 개수는 0으로 초기화
    if curr_size==already_eat:
        curr_size+=1
        already_eat=0

    # 다음 출발 지점을 정한다.
    start=(nx, ny, 0)

print(time)