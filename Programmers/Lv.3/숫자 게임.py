def solution(A, B):
    point = 0
    A.sort()
    B.sort()

    while A:
        a = A.pop()
        b = B.pop()

        if a < b:
            point += 1
        else:
            B.append(b)

    return point