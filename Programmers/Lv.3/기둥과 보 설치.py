def impossible(answer):
    COL, ROW = 0, 1

    for x, y, a in answer:
        if a == COL:  # 기둥일 때
            # 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 함.
            if y != 0 and [x, y - 1, COL] not in answer and [x - 1, y, ROW] not in answer and [x, y, ROW] not in answer:
                return True
        else:  # 보일 때
            # 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함.
            if [x, y - 1, COL] not in answer and [x + 1, y - 1, COL] not in answer and not (
                    [x - 1, y, ROW] in answer and [x + 1, y, ROW] in answer):
                return True
    return False


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, material, build = frame[0], frame[1], frame[2], frame[3]

        item = [x, y, material]
        if build:  # 설치
            answer.append(item)
            if impossible(answer):
                answer.remove(item)

        elif [x, y, material] in answer:  # 삭제
            answer.remove(item)
            if impossible(answer):
                answer.append(item)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))