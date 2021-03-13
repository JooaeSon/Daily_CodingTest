from collections import deque, defaultdict
import math
import sys

sys.setrecursionlimit(10 ** 6)


def find_parent(x, parent):
    if x == parent[x]:
        return x
    else:
        p = find_parent(parent[x], parent)
        parent[x] = p
        return p


def union_find(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    parent[y] = x


def bfs(land, start, visited, height, group):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        visited[y][x] = group
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(land) and 0 <= nx < len(land[0]) and visited[ny][nx] == 0 and abs(
                    land[ny][nx] - land[y][x]) <= height:
                visited[ny][nx] = group
                queue.append((ny, nx))


def find_height(visited, height, maps, table):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            rx = x + 1
            dy = y + 1
            # 오른쪽 값과 비교
            if rx < len(maps[0]) and visited[y][x] != visited[y][rx]:
                a, b = min(visited[y][x], visited[y][rx]), max(visited[y][x], visited[y][rx])
                table[(a, b)] = min(table[(a, b)], abs(maps[y][x] - maps[y][rx]))
            # 아래 값과 비교
            if dy < len(maps) and visited[dy][x] != visited[y][x]:
                a, b = min(visited[dy][x], visited[y][x]), max(visited[dy][x], visited[y][x])
                table[(a, b)] = min(table[(a, b)], abs(maps[dy][x] - maps[y][x]))


def solution(land, height):
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    group = 1

    # 1. land height별로 그룹핑
    for y in range(len(land)):
        for x in range(len(land[0])):
            if visited[y][x] == 0:
                bfs(land, (y, x), visited, height, group)
                group += 1

    # 2. 각 land별로 연결하는 최솟값 찾기
    table = defaultdict(lambda: math.inf)
    find_height(visited, height, land, table)
    table = sorted(table.items(), key=lambda x: x[1])
    answer = 0
    nodes = {i: i for i in range(1, group)}
    for (a, b), value in table:
        # 사다리로 연결
        if find_parent(a, nodes) != find_parent(b, nodes):
            union_find(a, b, nodes)
            answer += value

    return answer





# 참고: https://inspirit941.tistory.com/181
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