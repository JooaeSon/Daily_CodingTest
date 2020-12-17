import copy


def solution(triangle):
    answer = 0
    t = copy.deepcopy(triangle)

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            if (triangle[i][j] + t[i + 1][j]) >= triangle[i + 1][j]:
                triangle[i + 1][j] = triangle[i][j] + t[i + 1][j]

            if (triangle[i][j] + t[i + 1][j + 1]) >= triangle[i + 1][j + 1]:
                triangle[i + 1][j + 1] = triangle[i][j] + t[i + 1][j + 1]
    # print(triangle)
    return max(triangle[-1])