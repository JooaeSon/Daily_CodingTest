def solution(n, times):
    answer = 0
    left, right = 1, min(times) * n

    while left <= right:
        mid = (left + right) // 2
        temp = n
        for time in times:
            temp -= mid // time
            if temp <= 0:
                answer = mid
                right = mid - 1
                break

        if temp > 0:
            left = mid + 1

    return answer