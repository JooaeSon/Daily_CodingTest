import math


def solution(n, stations, w):
    result = 0
    distance = []

    # 설치된 기지국 사이에 전파가 닿지 않는 거리를 저장한다
    for i in range(1, len(stations)):
        distance.append((stations[i] - w - 1) - (stations[i - 1] + w))

    # 맨 앞 기지국에서 첫 번째 아파트 사이에 전파가 닿지 않는 거리,
    # 맨 뒤 기지국에서 마지막 아파트 사이에 전파가 닿지 않는 거리를 저장한다
    distance.append(stations[0] - w - 1)
    distance.append(n - (stations[-1] + w))

    for i in distance:
        # 닿지 않는 거리가 0 이하일 경우 스킵한다
        if i <= 0: continue
        # 닿지 않는 거리에 설치할 수 있는 최소개수를 더해준다.
        result += math.ceil(i / ((w * 2) + 1))
    return result