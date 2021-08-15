dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(cube, query):
    x1, y1, x2, y2 = query
    sx, sy, ex, ey = x1 - 1, y1 - 1, x2 - 1, y2 - 1

    curr_x, curr_y = sx, sy
    tmp = cube[curr_x][curr_y]
    for dir in range(4):
        while True:
            nx, ny = curr_x + dx[dir], curr_y + dy[dir]
            if not sx <= nx <= ex or not sy <= ny <= ey:
                break

            ntmp = cube[nx][ny]
            cube[nx][ny] = tmp
            tmp = ntmp
            curr_x, curr_y = nx, ny
            print(cube)

    return


def solution(rows, columns, queries):
    answer = []
    cube = []

    num = 1
    for _ in range(rows):
        lst = []
        for j in range(columns):
            lst.append(num)
            num += 1
        cube.append(lst)

    for query in queries:
        rotate(cube, query)
        answer.append(min(map(min, queries)))

    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])