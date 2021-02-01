def check(supoja, answers):
    cnt = 0
    answer_sheet = supoja * (len(answers) // len(supoja)) + supoja[:len(answers) % len(supoja)]

    for i in range(len(answer_sheet)):
        if answer_sheet[i] == answers[i]:
            cnt += 1

    return cnt


def solution(answers):
    answer = []
    answer_cnt = []
    supojas = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(len(supojas)):
        point = check(supojas[i], answers)
        answer_cnt.append((point, i + 1))

    answer_cnt = sorted(answer_cnt, key=lambda x: (-x[0], x[1]))

    pre_value = answer_cnt[0][0]
    answer.append(answer_cnt[0][1])
    for j in range(1, len(answer_cnt)):
        if pre_value == answer_cnt[j][0]:
            answer.append(answer_cnt[j][1])
        else:
            break

    return answer