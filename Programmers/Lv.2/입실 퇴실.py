from collections import *


def solution(enter, leave):
    answer = [0] * len(enter)
    room = []
    dic = {}

    enter = deque(enter)
    leave = deque(leave)

    for i in range(len(enter)):
        dic[i + 1] = set()

    while leave:
        cnt = 0
        while leave[0] not in room:
            room.append(enter.popleft())
            cnt += 1

        if cnt > 0:  # 사람이 새로 추가 될때만
            for i in range(len(room)):
                for j in range(len(room)):
                    if i != j:
                        dic[room[i]].add(room[j])

        room.remove(leave[0])
        leave.popleft()

    for key, value in dic.items():
        answer[key - 1] = len(value)

    return answer