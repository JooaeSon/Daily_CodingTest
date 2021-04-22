import copy

N, M, K = map(int, input().split())

board=[[list() for _ in range(N)] for _ in range(N)]

fireBalls=[]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r-=1
    c-=1
    fireBalls.append((r, c, m, s, d))
    board[r][c].append((m, s, d))

dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # 이동
    for i in range(len(fireBalls)):
        x, y, m, s, d = fireBalls[i]
        nx, ny = (x+s*dx[d])%N, (y+s*dy[d])%N
        board[x][y].remove((m, s, d))
        board[nx][ny].append((m, s, d))
        fireBalls[i] = (nx, ny, m, s, d)

    # 이동 후 2개 이상 파이어 볼 확인
    tmp_board=[[list() for _ in range(N)] for _ in range(N)]
    tmp_fireBalls=[]
    for i in range(N):
        for j in range(N):
            if len(board[i][j])>=2:
                mm, ss, nn = 0, 0, len(board[i][j]) # 합쳐지는 질량, 속도, 방향, 파이어볼 개수
                odd, even, flag = 0, 0, 0
                for idx, ball in enumerate(board[i][j]):
                    m, s, d = ball
                    mm+=m
                    ss+=s
                    if idx==0:
                        if d%2==0: even =1
                        else: odd = 1
                    else:
                        if even ==1 and d%2 ==1:
                            flag=1
                        elif odd==1 and d%2==0:
                            flag=1

                nm, ns = mm//5, ss//nn
                if nm==0: # 질량이 0일 때는 소멸
                    continue
                dir=[]
                if flag==0:
                    dir=[0, 2, 4, 6]
                else:
                    dir=[1, 3, 5, 7]
                
                for nd in dir:
                    tmp_fireBalls.append((i, j, nm, ns, nd))
                    tmp_board[i][j].append((nm, ns, nd))

            elif len(board[i][j])==1:
                tmp_board[i][j]=board[i][j]
                m, s, d = board[i][j][0]
                if (i, j, m, s, d) in fireBalls:
                    tmp_fireBalls.append((i, j, m, s, d))
    
    board=copy.deepcopy(tmp_board)
    fireBalls=copy.deepcopy(tmp_fireBalls)

# K번의 명령이 끝난 뒤
ans=0
for fireBall in fireBalls:
    x, y, m, s, d = fireBall
    ans+=m

print(ans)