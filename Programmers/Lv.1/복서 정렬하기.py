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

    print(win_heavier_count)
    print(win_rate)

    return answer