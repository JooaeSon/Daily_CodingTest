def solution(citations):
    answer = -987654321

    citations.sort()
    for h in reversed(range(0, 10001)):
        refer = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                refer += 1

        if refer >= h and h >= (len(citations) - refer):
            if answer < h:
                answer = h

    return answer