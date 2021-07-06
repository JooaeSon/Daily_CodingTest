def solution(d, budget):
    answer, SUM = 0, 0
    d.sort()

    for itm in d:
        if SUM + itm <= budget:
            SUM += itm
            answer += 1

    return answer