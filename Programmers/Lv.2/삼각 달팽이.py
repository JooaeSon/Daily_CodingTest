import itertools

def snail_pos(x, y, dirc):
    if dirc % 3 == 0:  # 아래
        x += 1
    elif dirc % 3 == 1:  # 오른쪽
        y += 1
    else:  # 위
        x -= 1
        y -= 1

    return x, y


def solution(n):
    tri_snail = [[0] * i for i in range(1, n + 1)]
    snail_direct = range(n)

    x, y = -1, 0
    num = 1
    for dirc in snail_direct:
        for _ in range(dirc, n):
            x, y = snail_pos(x, y, dirc)
            tri_snail[x][y] = num
            num += 1

    return list(itertools.chain(*tri_snail))