def judgement(player):
    player.sort()
    for i in range(len(player) - 2):
        # 연속인 숫자가 3개 이상이면 run
        if player[i] + 2 == player[i + 1] + 1 == player[i + 2]:
            return True
        # 같은 숫자가 3개 이상이면 triplet
        if player[i] == player[i + 1] == player[i + 2]:
            return True

    return False


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    lst = list(map(int, input().split()))
    p1, p2 = [], []

    for i in range(len(lst)):
        if i % 2 == 0:
            p1.append(lst[i])
            if judgement(p1):
                result = 1
                break
        else:
            p2.append(lst[i])
            if judgement(p2):
                result = 2
                break

    print(f'#{test_case} {result}')
