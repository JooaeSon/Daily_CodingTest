count = 0


def solution(n):
    global count

    dfs(0, 0, n)

    return count


def dfs(left, right, n):
    global count

    if left < right:
        return

    if left == n and right == n:
        count += 1
        return

    if left > n or right > n:
        return

    dfs(left + 1, right, n)
    dfs(left, right + 1, n)
