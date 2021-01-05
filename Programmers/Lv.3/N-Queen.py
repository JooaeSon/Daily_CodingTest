cnt = 0


def dfs(n, y, col, cross1, cross2):
    global cnt
    if -1 not in col:
        cnt += 1
        return

    for x in range(n):
        if col[x] == -1 and (x + y) not in cross1 and (x - y) not in cross2:
            col[x] = y
            cross1.add(x + y)
            cross2.add(x - y)
            dfs(n, y + 1, col, cross1, cross2)
            col[x] = -1
            cross1.remove(x + y)
            cross2.remove(x - y)


def solution(n):
    global cnt
    col = [-1] * n
    cross1 = set()
    cross2 = set()
    dfs(n, 0, col, cross1, cross2)

    return cnt