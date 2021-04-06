N, M = map(int, input().split())

# 0은 흰색, 1은 빨간색, 2는 파란색
board = [list(map(int, input().split())) for _ in range(N)]
playing = [[[] for _ in range(N)] for _  in range(N)]

horse = []
for i in range(M):  # 말 올려 놓기/ 초기 세팅
    x, y, dir = map(int, input().split())
    horse.append([x-1, y-1, dir-1])
    playing[x-1][y-1].append(i)


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

turn=0
flag=False
while True:
    if turn>1000:
        turn = -1
        break

    for i in range(M): # 하나의 턴
        x, y, dir = horse[i]
        nx, ny = x + dx[dir], y + dy[dir]  # 앞으로 움직일 좌표

        if not 0 <= nx < N or not 0 <= ny < N or board[nx][ny]==2:
            if 0<=dir<=1:
                ndir=(dir+1)%2
            else:
                ndir=(dir-1)%2+2
            horse[i][2]=ndir
            nx, ny = x + dx[ndir], y + dy[ndir]
            if not 0 <= nx < N or not 0 <= ny < N or board[nx][ny] == 2:
                continue
        play_set=[]
        for idx, key in enumerate(playing[x][y]):
            if key==i:
                play_set.extend(playing[x][y][idx:])
                playing[x][y] = playing[x][y][:idx]
                break

        if board[nx][ny]==1:
            play_set = reversed(play_set)

        for j in play_set:
            playing[nx][ny].append(j)
            horse[j][:2] = [nx, ny]

        if len(playing[nx][ny])>=4:
            flag=True
            break

    turn += 1
    if flag: # 게임 종료
        break

print(turn)