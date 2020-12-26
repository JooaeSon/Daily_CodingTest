def solution(n, s):
    if s//n == 0:
        return [-1]
    result = [s//n]*n # 분산이 가장 작은 값으로
    idx = len(result)-1

    for _ in range(s % n): #뒤에서부터 차례로 +1씩 더해주기
        result[idx] += 1
        idx -= 1

    return result