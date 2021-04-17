from collections import *

N, M, K = map(int, input().split())
board=[list(map(int, input().split())) for _ in range(N)]
smell_stamp=[[0]*N for _ in range(N)]

shark=defaultdict(list)
for i in range(N):
    for j in range(N):
        if board[i][j]:
            shark[board[i][j]-1].append((i, j, K))
            smell_stamp[i][j]=-1
print(shark)

# 상어 방향 정보
shark_dir=list(map(int, input().split()))
priority=[] # 방향 우선순위 담기
for i in range(M):
    lst=[]
    for j in range(4):
        tmp=list(map(int, input().split()))
        lst.append(tmp)
    priority.append(lst)

print(priority)
# 위, 아래, 왼, 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def removeSmell(routes): # 냄세 제거
    tmp=[]
    for i in range(len(routes)):
        x, y, smell = routes[i][0], routes[i][1], routes[i][2]
        smell-=1
        if smell!=0: #아직 냄새가 0이 아니라면
            tmp.append(routes[i])
        else:
            smell_stamp[x][y]=0

    return tmp


def move_shark(x, y, nx, ny, num, dir):
    board[x][y] = 0  # 떠나갈 위치
    # 만약 다른 상어가 이미 존재하는 자리가 아니거나 있어도 지금 상어 넘버가 더 작다면
    if not board[nx][ny] or (board[nx][ny] and board[nx][ny]>num+1):
        board[nx][ny] = num + 1  # 미래의 위치에 상어 놓기

    shark_dir[num] = dir + 1  # 방향 저장
    shark[num] = removeSmell(shark[num])
    shark[num].append((nx, ny, K))  # 새로 냄새 뿌리기
    smell_stamp[nx][ny] = -1 # 냄새 찍기

    return


time=0
while True:
    print("board: ", board)
    if time > 1000:
        time=-1
        break

    if sum(map(sum, board))==1:
        break

    for num in range(M): # 상어 번호
        pre_dir=shark_dir[num]-1 # 상어의 현재 방향
        one_shark_dir=priority[num][pre_dir]
        print(one_shark_dir)
        x, y, smell=shark[num][-1][0], shark[num][-1][1], shark[num][-1][2]
        impossible=0
        for dir in one_shark_dir:
            dir-=1
            nx, ny = x+dx[dir], y+dy[dir]
            print('nx:', nx, 'ny:', ny)
            if not 0<=nx<N or not 0<=ny<N or smell_stamp[nx][ny]:
                impossible+=1 # 냄새 방향 불가능 카운팅
                continue
            move_shark(x, y, nx, ny, num, dir)
            break

        if impossible==len(one_shark_dir):

            nx, ny = x + dx[pre_dir], y + dy[pre_dir]
            move_shark(x, y, nx, ny, num, pre_dir)

    time+=1

print(time)
