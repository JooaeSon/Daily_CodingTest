T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    tree = [0] * (N + 1)
    idx = 1
    for i in range(len(lst)):
        tree[idx] = lst[i]
        j = idx
        while j > 1: # 자식이 부모보다 작은 값이 있는지 조상들 탐색
            if tree[j] <= tree[j // 2]:
                tree[j], tree[j // 2] = tree[j // 2], tree[j]
            j //= 2

        idx += 1

    # 마지막 노드의 조상들의 저장된 합
    Sum = 0
    i = len(tree)-1
    while i > 0:
        i //= 2
        Sum += tree[i]

    print(f'#{test_case} {Sum}')
