def isPossible(stones, k, mid):
    chk = 0
    for stone in stones:
        if stone - mid <= 0:    # 연속해서 0이하인 징검다리 돌이 있는지 확인
            chk += 1
            if chk >= k:
                return False
        else:
            chk = 0
    else:
        return True


def solution(stones, k):
    answer = 0

    MIN, MAX = 1, max(stones)   # 최소, 최대 사람수
    while MIN <= MAX:   # 이분 탐색으로 진행
        mid = (MIN + MAX) // 2

        if isPossible(stones, k, mid):  # mid값이 가능한 값인지 확인
            answer = mid
            MIN = mid + 1
        else:
            MAX = mid - 1

    return answer + 1