def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)

    for stream in skill_trees:
        length = 0
        for s in stream:
            if s in skill:
                length = length + 1

        numbering = [0] * len(skill)
        cnt = 0
        for i in range(len(stream)):
            if stream[i] in skill:
                cnt = cnt + 1
                s_idx = skill.index(stream[i])
                numbering[s_idx] = cnt
        amount = 0

        for i in range(len(numbering)):
            if numbering[i] == i + 1:
                amount = amount + 1
        if amount == length:
            answer = answer + 1

    return answer