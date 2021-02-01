def solution(brown, yellow):
    brown_w = brown / 2 - 1
    yellow_w, yellow_h = yellow, 1

    cnt = 1
    while True:
        if brown_w - 2 == yellow_w:
            return [brown_w, yellow_h + 2]

        cnt += 1
        yellow_w = yellow / cnt
        yellow_h += 1

        brown_w -= 1
