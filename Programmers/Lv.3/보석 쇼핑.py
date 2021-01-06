def solution(gems):
    TYPE_NUM = len(set(gems))
    GEM_NUM = len(gems)
    shop_bag = {gems[0]: 1}
    cand = []
    start, end = 0, 0
    DIST, RESULT = 0, 1

    while start < GEM_NUM and end < GEM_NUM:
        if len(shop_bag) < TYPE_NUM:
            end += 1
            if end == GEM_NUM:
                break
            shop_bag[gems[end]] = shop_bag.get(gems[end], 0) + 1
        else:  # 가방이 종류 별 보석으로 다 채워졌다면
            cand.append((end - start, [start + 1, end + 1]))
            shop_bag[gems[start]] -= 1
            if shop_bag[gems[start]] == 0:
                del shop_bag[gems[start]]
            start += 1

    cand = sorted(cand, key=lambda x: (x[DIST], x[RESULT]))

    return cand[0][RESULT]