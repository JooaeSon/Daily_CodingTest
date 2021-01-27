def solution(w, h):
    # 최소 공약수 구하기
    G = 0
    for i in range(1, max(w, h) + 1):
        if w % i == 0 and h % i == 0:
            G = i

    return w * h - (w / G + h / G - 1) * G