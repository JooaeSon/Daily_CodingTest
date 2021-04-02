from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def end_game(b):
    if b.count("0") == 16:
        return True
    return False


def remove_element(b, e):
    b = b.replace(e, "0")
    return b


def move(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if 0 <= ny < 4 and 0 <= nx < 4 and b[ny * 4 + nx] == "0":
        return move(b, ny, nx, dy, dx)
    else:
        if 0 <= ny < 4 and 0 <= nx < 4:
            return (ny, nx)
        else:
            return (y, x)


def solution(board, r, c):
    answer = 0
    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])

    deq = deque([(r, c, b, 0, -1)])
    s = set()

    while deq:
        y, x, b, c, e = deq.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s:
            continue
        s.add((y, x, b, e))

        if end_game(b):
            return c

        # 4 방향 이동
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                deq.append((ny, nx, b, c + 1, e))

        # Ctrl + 4방향 이동
        for dy, dx in d:
            ny, nx = move(b, y, x, dy, dx)
            if ny == y and nx == x:
                continue
            deq.append((ny, nx, b, c + 1, e))

        # enter를 하는 경우
        if b[pos] != 0:
            if e == -1:
                n_e = pos
                deq.append((y, x, b, c + 1, n_e))
            else:
                if e != pos and b[e] == b[pos]:
                    b = remove_element(b, b[e])
                    deq.append((y, x, b, c + 1, -1))

    return answer

# 참고: https://walwal234.tistory.com/37