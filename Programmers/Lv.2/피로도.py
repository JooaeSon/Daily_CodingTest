result = float('inf')


def dfs(dungeon, k, count, N):
    global result

    if k < dungeon[0] or count > N:
        return
    count += 1
    dfs(dungeon, k, count, N)
    count -= 1
    return


def solution(k, dungeons):
    global result
    N = len(dungeons)

    for dungeon in dungeons:
        dfs(dungeon, k, 0, N)

    return result