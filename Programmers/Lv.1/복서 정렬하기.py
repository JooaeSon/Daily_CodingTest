def solution(weights, head2head):
    answer = []
    N = len(weights)
    win_rate = []
    win_heavier_count = []

    for i in range(N):
        info = head2head[i]
        if not N - info.count('N'):
            win_rate.append(0)
        else:
            win_rate.append(info.count('W') / (N - info.count('N')))

        heaviear = 0
        for j in range(N):
            if info[j] == 'W' and weights[i] < weights[j]:
                heaviear += 1
        win_heavier_count.append(heaviear)

    for i in range(N):
        answer.append((win_rate[i], win_heavier_count[i], weights[i], i))

    answer = sorted(answer, key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    return [answer[i][3] + 1 for i in range(N)]