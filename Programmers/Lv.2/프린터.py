from collections import deque


def solution(priorities, location):
    answer = 0
    li = []

    for i, v in enumerate(priorities):
        li.append((i, v))
    print(li)
    q = deque(li)
    cnt = 0

    while q:
        idx, priority = q.popleft()
        maxVal = max(priorities)

        if priority < maxVal:
            q.append((idx, priority))
            continue

        else:
            priorities.remove(maxVal)
            cnt += 1

            if idx == location:
                return cnt