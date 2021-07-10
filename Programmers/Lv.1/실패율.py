def solution(N, stages):
    answer = []

    dic = {}
    for key in stages:
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1

    player = len(stages)  # 참가자 수
    for i in range(1, N + 1):  # 1단계 부터 N단계까지 실패율 구하기
        if i in dic:
            answer.append([(dic[i] / player), i])
            player -= dic[i]
        else:
            answer.append([0, i])

    answer.sort(key=lambda x: (-x[0], x[1]))

    return [a[1] for a in answer]