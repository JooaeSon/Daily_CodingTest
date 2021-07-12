def solution(n):
    answer = 0
    ternary = ''

    while n:
        ternary += str(n % 3)
        n //= 3

    for i in reversed(range(len(ternary))):
        answer += int(ternary[i]) * (3 ** (len(ternary) - i - 1))

    return answer