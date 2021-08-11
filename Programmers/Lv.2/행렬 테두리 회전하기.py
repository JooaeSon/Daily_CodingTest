dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate(query):
    x1, y1, x2, y2 = query

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