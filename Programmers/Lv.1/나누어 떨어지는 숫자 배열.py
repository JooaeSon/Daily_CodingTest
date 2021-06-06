def solution(arr, divisor):
    answer = []
    key = 0
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            key += 1

    if key == 0:
        answer.append(-1)
    answer.sort()

    return answer