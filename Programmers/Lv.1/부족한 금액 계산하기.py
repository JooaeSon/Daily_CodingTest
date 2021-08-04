def solution(price, money, count):
    answer = 0

    for i in range(1, count + 1):
        answer += price * i

    return answer - money if answer - money > 0 else 0