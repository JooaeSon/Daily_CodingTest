def dfs(x, y):
    global stack, result
    stack.append((x, y))
    #print("stack:", stack)
    if miro[x][y] == 3:
        result = 1
        return

    for i in range(1, 5):
        if i == 1 and x-1 >= 0 and (miro[x-1][y] == 0 or miro[x-1][y] == 3):
            if miro[x-1][y] == 0:
                miro[x-1][y] = -1
            dfs(x-1, y)
        elif i == 2 and x+1 < N and (miro[x+1][y] == 0 or miro[x+1][y] == 3):
            if miro[x + 1][y] == 0:
                miro[x + 1][y] = -1
            dfs(x+1, y)
        elif i == 3 and y-1 >= 0 and (miro[x][y-1] == 0 or miro[x][y-1] == 3):
            if miro[x][y-1] == 0:
                miro[x][y - 1] = -1
            dfs(x, y-1)
        elif i == 4 and y+1 < N and (miro[x][y+1] == 0 or miro[x][y+1] == 3):
            if miro[x][y+1] == 0:
                miro[x][y + 1] = -1
            dfs(x, y+1)

    stack.pop()
    return


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    stack = []

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2: # 출발지점 저장
                start_x = i
                start_y = j
            elif miro[i][j] == 3: # 도착지점 저장
                end_x = i
                end_y = j

    dfs(start_x, start_y)

    print(f'#{test_case} {result}')
