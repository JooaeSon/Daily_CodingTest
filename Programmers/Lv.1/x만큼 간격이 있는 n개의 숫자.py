def solution(x, n):
    answer = []

    for i in range(1, n + 1):
        a = x * i
        answer.append(a)

    return answer