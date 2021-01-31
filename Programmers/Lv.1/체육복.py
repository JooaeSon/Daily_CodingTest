def solution(n, lost, reserve):

    std = [i for i in range(1, n + 1)]
    lost.sort()
    reserve.sort()
    std = set(std) - set(lost)

    for i in range(len(lost)):
        if lost[i] in reserve:  # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
            reserve[reserve.index(lost[i])] = -1
            std.add(lost[i])

    for i in range(len(lost)):
        if lost[i] - 1 in reserve and reserve[reserve.index(lost[i] - 1)] != -1:
            reserve[reserve.index(lost[i] - 1)] = -1
            std.add(lost[i])

        elif lost[i] + 1 in reserve and reserve[reserve.index(lost[i] + 1)] != -1:
            reserve[reserve.index(lost[i] + 1)] = -1
            std.add(lost[i])

    return len(std)