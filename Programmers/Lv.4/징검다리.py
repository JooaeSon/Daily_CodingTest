def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        remove = 0
        m_min = float('inf')
        for rock in rocks:
            if rock - pre_rock < mid:
                remove += 1  # 바위 제거
            else:
                m_min = min(m_min, rock - pre_rock)
                pre_rock = rock

        if remove > n:  # 너무 많이 제거되었을 경우
            right = mid - 1
        else:  # 아직 n 보다는 적게 제거되었을 경우
            answer = mid
            left = mid + 1

    return answer