
'''
# 오류 였던 코드
from collections import deque

group = [{(0, 0)}]


def Grouping(x, y, dx, dy, signal, land, height):
    global group

    if signal == 'not need':  # 사다리가 필요 없을 경우 같은 그룹으로 그룹핑
        for g_set in group:
            if (x, y) in g_set:
                g_set.add((x + dx, y + dy))
                break

    else:  # 사다리가 필요할 경우 다른 그룹으로 그룹핑
        for g_set in group:
            nx, ny = 0, 0
            for tmpx, tmpy in g_set:
                nx, ny = tmpx, tmpy  # 첫번째 숫자 꺼내오기
                break
            differ = abs(land[nx][ny] - land[x + dx][y + dy])
            if differ <= height:  # 비슷한 애 찾기
                g_set.add((x + dx, y + dy))
                break
        else:
            group.append({(x + dx, y + dy)})
    return


def solution(land, height):
    global group
    answer = 0
    ladder = [[float('inf')] * len(land) for _ in range(len(land))]
    visited = set()

    deq = deque([(0, 0)])
    while deq:
        x, y = deq.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))  # 방문 체크
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            if 0 <= x + dx < len(land) and 0 <= y + dy < len(land):
                differ = abs(land[x][y] - land[x + dx][y + dy])
                if differ <= height:  # 사다리가 필요 없을 경우
                    Grouping(x, y, dx, dy, 'not need', land, height)
                else:  # 사다리가 필요한 경우
                    # 새로운 경계 생성
                    ladder[x + dx][y + dy] = differ  # 가고자 하는 위치 칸에 차이값 넣기
                    Grouping(x, y, dx, dy, 'need', land, height)
                x += dx
                y += dy
                deq.append((x, y))
    print("group:", group)
    print("ladder:", ladder)
    for g_set in group:
        mmin = float('inf')
        for x, y in g_set:
            if ladder[x][y] < mmin:
                mmin = ladder[x][y]
        answer += mmin

    return answer

'''