def solution(table, languages, preference):
    answer = []

    for row in table:
        Sum = 0
        stream = list(row.split())

        jobs = stream[0]
        for i in range(len(stream[1:])):
            if stream[1:][i] in languages:
                idx = languages.index(stream[1:][i])
                Sum += preference[idx] * (len(stream[1:]) - i)

        answer.append((jobs, Sum))

    return sorted(answer, key=lambda x: (-x[1], x[0]))[0][0]