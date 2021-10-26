result = float('-inf')


def dfs(dungeons, k, count, visited):
    global result

    for idx, dungeon in enumerate(dungeons):
        if not visited[idx] and k >= dungeons[idx][0]:
            visited[idx] = 1
            dfs(dungeons, k - dungeon[1], count + 1, visited)
            visited[idx] = 0

    result=max(count, result)


def solution(k, dungeons):
    global result

    visited = [0 for _ in range(len(dungeons))]
    dfs(dungeons, k, 0, visited)
    print(result)
    return result

solution(80, [[80,20],[50,40],[30,10]])