dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(query):
    x1, y1, x2, y2 = query
    sx, sy, ex, ey = x1 - 1, y1 - 1, x2 - 1, y2 - 1

    curr_x, curr_y = sx, sy
    for dir in range(4):
        while True:
            nx, ny = curr_x + dx[dir], curr_y + dy[dir]
            if not sx <= nx <= ex or not sy <= ny <= ey:
                break
            curr_x, curr_y = nx, ny

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
        rotate(query)
        answer.append(min(map(min, queries)))

    return answer