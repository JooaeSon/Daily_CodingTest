def solution(N, number):
    answer = 0
    if N == number:
        return 1

    # N set()으로 초기화
    lst = [set() for i in range(8)]

    # N을 사용했을 때 나올 수 있는 수 정리
    for i in range(8):
        lst[i].add(int(str(N) * (i + 1)))

    # 사칙 연산 적용(+, -, *, //)
    for i in range(8):
        for j in range(i):
            for op1 in lst[j]:
                for op2 in lst[i - j - 1]:
                    lst[i].add(op1 + op2)
                    lst[i].add(op1 * op2)
                    lst[i].add(op1 - op2)
                    if op2 != 0:
                        lst[i].add(op1 // op2)
        if number in lst[i]:
            answer = i + 1
            break
    else:
        return -1

    return answer