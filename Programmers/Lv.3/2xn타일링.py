def solution(n):
    D = [0] * (n + 1)
    for i in range(1, len(D)):
        if i == 1:
            D[i] = 1
        elif i == 2:
            D[i] = 2
        else:
            D[i] = (D[i - 1] + D[i - 2]) % 1000000007

    return D[n]