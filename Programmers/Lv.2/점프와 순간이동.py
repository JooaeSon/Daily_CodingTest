def solution(n):
    battery = 0
    # 순간이동을 할 경우(현재 온 거리*2)
    # K칸을 앞으로 점프(건전지 사용량++K만큼)
    tmp = n
    telepo = []
    while tmp > 1:
        tmp = tmp // 2
        telepo.append(tmp)

    d = 0
    while d < n:
        if d in telepo:
            d = d * 2
        else:
            d += 1
            battery += 1

    return battery