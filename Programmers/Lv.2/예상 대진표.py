def competition(num):
    if num % 2 == 0:
        num = num // 2
    else:
        num = num // 2 + 1
    return num


def solution(n, a, b):
    rounded = 0

    while True:
        if (a % 2 == 0 and a == b + 1) or (a % 2 != 0 and b == a + 1):
            break
        a = competition(a)
        b = competition(b)
        rounded += 1

    return rounded + 1