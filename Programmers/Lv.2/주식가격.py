def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i, len(prices)):
            if j != i:
                cnt = cnt + 1
                if prices[i] > prices[j]:
                    break
        answer.append(cnt)
    return answer