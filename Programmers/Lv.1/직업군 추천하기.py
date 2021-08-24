from collections import defaultdict


def solution(table, languages, preference):
    answer = ''
    dic = defaultdict(list)
    Sum = 0
    for row in table:
        stream = list(row.split())
        print(stream)
        dic[stream[0]] = stream[1:]
        for st in stream[1:]:
            if st in languages:
                idx = languages.index(st)
                Sum += preference[idx]

    print(dic)
    return answer