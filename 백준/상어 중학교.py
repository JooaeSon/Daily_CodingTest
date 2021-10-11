from collections import *

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def isInGroup(): # 격자에 그룹이 존재하는지 확인
    '''
    그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다.
    검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다.
    그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며,
    임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다.
    '''


    return True


def playGravity():

    for j in range(N):
        pivot=N-1
        for i in reversed(range(N)):
            if board[i][j]==-1:
                pivot=i
            elif board[i][j]!=-1 and board[i][j]!='':
                board[pivot+1][j]=board[i][j]
                board[i][j]=''
                pivot=i


    return


def bfs(x, y, area, dic):
    # 기준 px, py
    px, py = x, y
    COLOR=board[px][py]
    deq = deque([(px, py)])
    dic[(px, py)] = list()  # 기준 시작 좌표에 해당하는 경로 모두 담기 위해
    print("sx:", x, "sy:", y)
    cnt, rainbow =0, 0
    while deq:
        x, y=deq.popleft()

        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            # 범위 안에 있고 아직 방문하지 않았어야 했고 검은블록(-1) 이 아니여야 한다.
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and board[nx][ny]!=-1:
                if not board[nx][ny]==0 and not board[nx][ny]==COLOR:
                    continue
                if board[nx][ny]==0: # 무지개 블록 갯수
                    rainbow+=1
                deq.append((nx, ny))
                dic[(px, py)].append((nx, ny)) # 지나간 좌표 표시/그룹에 속한 좌표 나중에 찾으려고
                visited[nx][ny] = -1
                cnt+=1 # 전체 블록 갯수

    # 블록 수 > 무지개 블록 수 > 행 번호 > 열 번호
    area.append((cnt, rainbow, px, py))
    print("***area:", area)
    
    return dic, area


# while True:
    # 방문 블록 초기화
visited = [[0 for _ in range(N)] for _ in range(N)]
dic = {}
area = []  # 블록 그룹 정보 초기화

# 격자에 그룹이 존재하는지 확인하기
"""
if not isInGroup():
    break
    """

# 1. 크기가 가장큰 블록 그룹 찾기, area정렬 순서에 따라 가장 앞에 있는 요소 가져오기
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j]!=-1 and board[i][j]!=0:
            dic, area=bfs(i, j, area, dic)

area=sorted(area, key=lambda x:(-x[0], -x[1], -x[2], -x[3]))
print("area:", area)
print("dic:", dic)
rmove_block_lst=dic[(area[0][2], area[0][3])]

"""
# 2. 1에서 찾은 블록 그룹 모두 제거
for x, y in rmove_block_lst:
    board[x][y] = ''

ans+=len(rmove_block_lst)**2 # 블록수^2만큼 점수 획득
"""
"""
    # 3. 격자에 중력이 작용
    playGravity()

    # 4. 격자가 90도 반시계 방향으로 회전
    board=list(zip(*board))[::-1]

    # 5. 다시 격자에 중력이 작용
    playGravity()
    """

print(ans)