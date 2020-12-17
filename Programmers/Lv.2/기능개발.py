from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    deq = deque()

    for i in range(len(progresses)):
        day = (100 - progresses[i]) / speeds[i]
        if day % 1 != 0:
            day = math.floor(day) + 1
        deq.append(int(day))

    while deq:
        val = deq.popleft()
        cnt = 1

        while deq:

            d = deq.popleft()
            if d > val:
                deq.appendleft(d)
                break
            cnt += 1
        answer.append(cnt)

    return answer