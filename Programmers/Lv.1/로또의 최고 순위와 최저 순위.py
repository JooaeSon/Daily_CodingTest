def cal(winPoint):
    if winPoint == 6:
        return 1
    elif winPoint == 5:
        return 2
    elif winPoint == 4:
        return 3
    elif winPoint == 3:
        return 4
    elif winPoint == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []

    cnt = 0
    for num in win_nums:
        if num in lottos:
            cnt += 1
    zero = lottos.count(0)

    return [cal(cnt + zero), cal(cnt)]