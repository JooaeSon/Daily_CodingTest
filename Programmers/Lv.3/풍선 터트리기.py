def solution(a):
    # 맨 앞, 맨 뒤 풍선은 어떻게든 남길 수 있다.
    # 가운데에 있는 풍선은, 자신을 둘러싼 풍선의 최솟값보다 작다면 남을 수 있다.
    answer = len(a)
    left, right = float('inf'), float('inf')
    maps = [[0 for _ in range(len(a))] for _ in range(2)]

    # 인접한 풍선 중 번호가 큰 풍선을 터트린다.
    # 왼쪽 기준으로, 번호가 작은 풍선을 남기는 경우
    for i in range(len(a)):
        if left > a[i]:
            left = a[i]
        maps[0][i] = left

    # 오른쪽 기준으로, 번호가 작은 풍선을 남기는 경우
    for i in range(len(a) - 1, -1, -1):
        if right > a[i]:
            right = a[i]
        maps[1][i] = right

    # 풍선을 남기는 것이 불가능한 경우: 오른쪽, 왼쪽 각각 최소값이 타겟 값보다 작은 경우
    for i in range(len(a)):
        if a[i] > maps[0][i] and a[i] > maps[1][i]:
            answer -= 1

    return answer