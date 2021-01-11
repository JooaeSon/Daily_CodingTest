def solution(cacheSize, cities):
    time = 0
    cities = [city.lower() for city in cities]
    cache = []
    # cacheSize가 0이면 cache miss로 판별
    if cacheSize == 0:
        time += len(cities) * 5
    else:
        for city in cities:
            # 도시가 캐시에 이미 있는 경우
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            # 도시가 캐시에 없는 경우
            else:
                # 캐시가 꽉찬 경우
                if len(cache) == cacheSize:
                    cache.pop(0)
                time += 5
                cache.append(city)

    return time