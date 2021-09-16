from collections import deque


def solution(enter, leave):
    answer = [0] * len(enter)
    room = []

    enter = deque(enter)
    leave = deque(leave)

    while leave:
        cnt = 0
        while leave[0] not in room:
            room.append(enter.popleft())
            cnt += 1

        print(room)
        print("cnt:", cnt)

        if cnt > 0:
            for idx in room:
                print("idx:", idx)
                answer[idx - 1] += cnt

        room.remove(leave[0])
        leave.popleft()

    return answer

solution([1, 4, 2, 3], [2, 1, 3, 4])