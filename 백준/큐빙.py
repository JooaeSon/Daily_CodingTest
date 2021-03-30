import sys

input = sys.stdin.readline

def cube(side, dir):
    global u, d, f, b, l, r
    if side == 'U' or side == 'D':
        if side == 'U':
            u = turn(u, dir)
            i, j = 2, 0
        else:
            d = turn(d, dir)
            i, j = 0, 2
        temp_l = [list(x) for x in zip(*l)]
        temp_r = [list(x) for x in zip(*r)]
        temp = b[i]
        if (side == 'U' and dir == '+') or (side == 'D' and dir == '-'):
            b[i] = list(reversed(temp_l[i]))
            temp_l[i] = f[j]
            f[j] = list(reversed(temp_r[j]))
            temp_r[j] = temp
        else:
            b[i] = temp_r[j]
            temp_r[j] = list(reversed(f[j]))
            f[j] = temp_l[i]
            temp_l[i] = list(reversed(temp))
        l = [list(x) for x in zip(*temp_l)]
        r = [list(x) for x in zip(*temp_r)]

    elif side == 'F' or side == 'B':
        if side == 'F':
            f = turn(f, dir)
            i = 2
        else:
            b = turn(b, dir)
            i = 0
        temp = u[i]
        if (side == 'F' and dir == '+') or (side == 'B' and dir == '-'):
            u[i] = l[i]
            l[i] = d[i]
            d[i] = r[i]
            r[i] = temp
        else:
            u[i] = r[i]
            r[i] = d[i]
            d[i] = l[i]
            l[i] = temp

    elif side == 'L' or side == 'R':
        if side == 'L':
            l = turn(l, dir)
            i, j = 0, 2
        else:
            r = turn(r, dir)
            i, j = 2, 0
        temp_u = [list(x) for x in zip(*u)]
        temp_d = [list(x) for x in zip(*d)]
        temp_f = [list(x) for x in zip(*f)]
        temp_b = [list(x) for x in zip(*b)]
        temp = temp_b[i]
        if (side == 'L' and dir == '+') or (side == 'R' and dir == '-'):
            temp_b[i] = list(reversed(temp_d[j]))
            temp_d[j] = list(reversed(temp_f[i]))
            temp_f[i] = temp_u[i]
            temp_u[i] = temp
        else:
            temp_b[i] = temp_u[i]
            temp_u[i] = temp_f[i]
            temp_f[i] = list(reversed(temp_d[j]))
            temp_d[j] = list(reversed(temp))
        u = [list(x) for x in zip(*temp_u)]
        d = [list(x) for x in zip(*temp_d)]
        f = [list(x) for x in zip(*temp_f)]
        b = [list(x) for x in zip(*temp_b)]


def turn(side, dir):
    print(side)
    print(*side)
    if dir == '+':
        return [list(reversed(x)) for x in zip(*side)]
    else:
        side = [list(x) for x in zip(*side)]
        temp = side[0]
        side[0] = side[2]
        side[2] = temp
        return side


tc = int(input())
for _ in range(tc):
    u = [['w' for _ in range(3)] for _ in range(3)]
    d = [['y' for _ in range(3)] for _ in range(3)]
    f = [['r' for _ in range(3)] for _ in range(3)]
    b = [['o' for _ in range(3)] for _ in range(3)]
    l = [['g' for _ in range(3)] for _ in range(3)]
    r = [['b' for _ in range(3)] for _ in range(3)]

    n = int(input())
    case = list(input().strip().split())
    for k in case:
        side, dir = list(k)
        cube(side, dir)
    for s in u:
        print(''.join(s))

# 참고: https://chldkato.tistory.com/148