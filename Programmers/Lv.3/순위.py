from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for result in results:
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])

    for i in range(1, n + 1):
        # i한테 진 애들은 i가 진 애들 한테도 진다.
        for loser in win[i]:
            lose[loser].update(lose[i])

        # i한테 이긴 애들은 i가 이긴 애들한테도 이긴다.
        for winner in lose[i]:
            win[winner].update(win[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1

    return answer