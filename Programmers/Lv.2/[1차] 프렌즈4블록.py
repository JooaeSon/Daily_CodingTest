def bfs(m, n, board):
    x, y=0, 0
    DELTA=[(0, 0), (1, 0), (0, 1), (1, 1)]
    del_info=set()
    # bfs search
    while True:
        for i in range(4):
            dy, dx = DELTA[i]
            if board[y][x]!=board[y+dy][x+dx] or board[y][x]=='x':
                break
        else:
            del_info.add((y, x))
            del_info.add((y+1, x))
            del_info.add((y, x+1))
            del_info.add((y+1, x+1))

        if x+1 == m-1 and y+1 != n-1:
            x=0
            y+=1
        elif x+1 < m-1:
            x+=1
        elif y+1 == n-1:
            break

    # board_set
    for y, x in del_info:
        board[y][x]=0
    # board_update
    for i, row in enumerate(board):
        empty=['x']*row.count(0)
        board[i]=empty+[block for block in row if block!=0]

    return len(del_info)

def solution(m, n, board):
    cnt = 0
    b=list(map(list,zip(*board)))

    while True:
        # bfs로 정사각형 4개 모양의 블록 찾기
        del_cnt=bfs(m, n, b)
        if del_cnt==0: # 더 이상 삭제 시킬 것이 없음
            return cnt
        cnt+=del_cnt