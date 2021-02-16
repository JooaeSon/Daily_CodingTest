from collections import deque


def chmode(begin, word):
    differ = 0
    for i in range(len(begin)):
        if begin[i] != word[i]:
            differ += 1

    if differ == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0

    deq = deque()
    cnt = 0
    while words:
        if begin == target:
            return cnt

        for word in words:
            if chmode(begin, word):
                deq.append((word, cnt + 1))

        begin, cnt = deq.popleft()