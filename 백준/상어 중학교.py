from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def isInGroup(): # 격자에 그룹이 존재하는지 확인

    return True


def bfs(x, y):
    # 기준 x, y
    deq = deque([(x, y)])
    cnt, rainbow =0, 0
    while deq:
        x, y=deq.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            # 범위 안에 있고 아직 방문하지 않았어야 했고 검은블록(-1) 이 아니여야 한다.
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and board[nx][ny]!=-1:
                if board[nx][ny]==0: # 무지개 블록 갯수
                    rainbow+=1
                deq.append((nx, ny))
                visited[nx][ny] = -1
                cnt+=1 # 전체 블록 갯수

    # 가장 큰 블록 > 무지개 블록 수 > 행 번호 > 열 번호
    area.append((cnt, rainbow, x, y))
    
    return


while True:
    # 방문 블록 초기화
    visited = [[0 for _ in range(N)] for _ in range(N)]
    area = [] # 블록 그룹 정보 초기화
    # 격자에 그룹이 존재하는지 확인하기
    if not isInGroup():
        break
    
    # 1. 크기가 가장큰 블록 그룹 찾기, area정렬 순서에 따라 가장 앞에 있는 요소 가져오기
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j]!=-1:
                bfs(i, j)
                
    # 2. 1에서 찾은 블록 그룹 모두 제거, 블록수^2만큼 점수 획득
    # 3. 격자에 중력이 작용
    # 4. 격자가 90도 반시계 방향으로 회전
    # 5. 다시 격자에 중력이 작용

print(ans)