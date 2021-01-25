from collections import deque

def BFS(start_x, start_y, G):
    global end_x, end_y
    deq.append((start_x, start_y))
    G[start_x][start_y] = -1

    while deq:
        #print(deq)
        x, y = deq.popleft()
        #print("G:", G)

        for i in range(1, 5):
            if i == 1 and y - 1 >= 0 and (G[x][y-1] == 0 or G[x][y-1] == 3):
                deq.append((x, y - 1))  # 좌
                G[x][y-1] = -1
                distance[x][y-1] = distance[x][y] + 1

            elif i == 2 and y + 1 < N and (G[x][y + 1] == 0 or G[x][y + 1] == 3):
                deq.append((x, y + 1))  # 우
                G[x][y + 1] = -1
                distance[x][y + 1] = distance[x][y] + 1

            elif i == 3 and x - 1 >= 0 and (G[x-1][y] == 0 or G[x-1][y] == 3):
                deq.append((x - 1, y))  # 상
                G[x-1][y] = -1
                distance[x-1][y] = distance[x][y] + 1

            elif i == 4 and x + 1 < N and (G[x + 1][y] == 0 or G[x + 1][y] == 3):
                deq.append((x + 1, y))  # 하
                G[x + 1][y] = -1
                distance[x + 1][y] = distance[x][y] + 1

        if x == end_x and y == end_y:
            break

    return

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    G = [list(map(int, input())) for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    deq = deque()

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    for i in range(N):
        for j in range(N):
            if G[i][j] == 2:
                start_x = i
                start_y = j
            elif G[i][j] == 3:
                end_x = i
                end_y = j

    BFS(start_x, start_y, G)

    if distance[end_x][end_y] != 0:
        print(f'#{test_case} {(distance[end_x][end_y])-1}')
    else:
        print(f'#{test_case} {(distance[end_x][end_y])}')
