from collections import deque


def solution(n, words):
    talked = []

    deq = deque(words)
    word = deq.popleft()
    while deq:
        talked.append(word)

        if deq[0] not in talked and word[-1] == deq[0][0]:
            word = deq.popleft()
        else:
            return [len(talked) % n + 1, len(talked) // n + 1]
    else:
        return [0, 0]