def solution(n):
    answer = 0

    if (n ** 0.5) % 1 == 0:  # 1로 나눈 나머지가 0이 아니라면 그것은 정수가 아니다.
        a = int(n ** 0.5)  # 정수인 소수점이 붙어있으면 int를 사용하여 형변환하기.

        if type(a) == int:
            answer = int((n ** 0.5 + 1) ** 2)
    else:
        answer = -1

    return answer