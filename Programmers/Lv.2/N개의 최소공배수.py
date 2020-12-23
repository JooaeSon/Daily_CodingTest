def solution(arr):
    arr.sort()
    lastNum = arr[-1]  # 제일 큰수가 최소 배수가 되는 것 부터 시작

    i = 1
    while True:
        LM = lastNum * i
        for n in arr:
            if LM % n != 0:
                break
        else:
            return LM
        i += 1