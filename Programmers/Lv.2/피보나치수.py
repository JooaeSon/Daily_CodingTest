def solution(n):
    numlst = [0] * (n + 1)

    for i in range(len(numlst)):
        if i == 0:
            numlst[0] = 0
        elif i == 1:
            numlst[1] = 1
        else:
            numlst[i] = (numlst[i - 1] + numlst[i - 2]) % 1234567

    return numlst[-1]