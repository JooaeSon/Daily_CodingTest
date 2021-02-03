from collections import deque


def solution(people, limit):
    boat = 0
    people.sort()
    q = deque(people)

    while q:
        if len(q) >= 2:  # 2명 이상 사람이 남았을때
            if q[0] + q[-1] <= limit:  # 제한 무게 이하일 때
                q.popleft()
        q.pop()
        boat += 1

    return boat