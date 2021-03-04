def press(s):
    n = len(s)
    if n == 1:
        return s[0][0]

    temp = [[] for _ in range(n // 2)]

    for i in range(1, n, 2):
        for j in range(1, n, 2):
            zero = s[i][j][0] + s[i][j - 1][0] + s[i - 1][j][0] + s[i - 1][j - 1][0]
            one = s[i][j][1] + s[i][j - 1][1] + s[i - 1][j][1] + s[i - 1][j - 1][1]

            if zero == 0: one = 1
            if one == 0: zero = 1

            temp[i // 2].append([zero, one])

    return press(temp)


def solution(arr):
    n = len(arr)
    init = [[] for _ in range(n // 2)]

    for i in range(1, n, 2):
        for j in range(1, n, 2):
            temp = [arr[i][j], arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1]]
            zero = temp.count(0)
            one = temp.count(1)

            if zero == 0: one = 1
            if one == 0: zero = 1

            init[i // 2].append([zero, one])

    return press(init)

# 참고> https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EC%BF%BC%EB%93%9C%EC%95%95%EC%B6%95-%ED%9B%84-%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0