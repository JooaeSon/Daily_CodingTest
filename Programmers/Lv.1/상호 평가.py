def cal(point):
    if point >= 90:
        return 'A'
    elif 80 <= point < 90:
        return 'B'
    elif 70 <= point < 80:
        return 'C'
    elif 50 <= point < 70:
        return 'D'
    else:
        return 'F'


def solution(scores):
    answer = ''
    scores = list(map(list, zip(*scores)))

    for i in range(len(scores)):
        if (scores[i][i] == max(scores[i]) and scores[i].count(max(scores[i])) == 1) or (scores[i][i] == min(scores[i]) and scores[i].count(min(scores[i])) == 1):
            scores[i][i] = 0

    idx = 0
    for stdSc in scores:
        if stdSc[idx] == 0:
            N = len(scores) - 1
        else:
            N = len(scores)
        answer += cal(sum(stdSc) / N)
        idx += 1

    return answer