answer = 0


def dfs(numbers, target, Sum, idx):
    global answer

    if idx == len(numbers):
        if Sum == target:
            answer += 1
        return

    for i in range(2):
        if i == 0:
            dfs(numbers, target, Sum - numbers[idx], idx + 1)
        else:
            dfs(numbers, target, Sum + numbers[idx], idx + 1)


def solution(numbers, target):
    global answer

    dfs(numbers, target, 0, 0)

    return answer