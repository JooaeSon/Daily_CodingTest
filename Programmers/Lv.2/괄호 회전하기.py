from collections import deque
import copy


def solution(s):
    answer = 0
    deq = deque(list(s))

    cnt = 0
    while cnt < len(s):
        deq.rotate(-1)

        sdeq = copy.deepcopy(deq)
        stack = []
        while sdeq:
            ch = sdeq.pop()
            if not stack:
                stack.append(ch)
            else:
                if (stack[-1] == '}' and ch == '{') or (stack[-1] == ')' and ch == '(') or (
                        stack[-1] == ']' and ch == '['):
                    stack.pop()
                else:
                    stack.append(ch)

        if not stack: answer += 1

        cnt += 1

    return answer