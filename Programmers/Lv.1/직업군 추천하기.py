def solution(table, languages, preference):
    answer = ''

    for row in table:
        Sum = 0
        stream = list(row.split())
        print(stream)
        jobs = stream[0]
        for i in range(len(stream[1:])):
            if stream[1:][i] in languages:
                print(stream[1:][i])
                idx = languages.index(stream[1:][i])
                Sum += preference[idx] * (len(stream[1:]) - 1)
        print(Sum)

    return answer