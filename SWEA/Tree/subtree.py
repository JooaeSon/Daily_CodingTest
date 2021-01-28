def findTree(num):
    global cnt
    cnt += 1

    # 트리의 양쪽에 다 값이 있을 경우
    if tree[0][num] != 0 and tree[1][num] != 0:
        findTree(tree[0][num])
        findTree(tree[1][num])
        return
    # 트리의 왼쪽에만 값이 있을 경우
    if tree[0][num] != 0:
        return findTree(tree[0][num])
    elif tree[1][num] != 0:
        return findTree(tree[1][num])
    # 트리 양쪽에 값이 없을 경우: 종료
    if tree[0][num] == 0 and tree[1][num] == 0:
        return

T = int(input())

for test_case in range(1, T + 1):
    cnt = 0
    E, N = map(int, input().split())
    info_lst = list(map(int, input().split()))
    tree = [[0] * (E + 2) for i in range(2)]

    for i in range(E):
        parent, child = info_lst[2 * i], info_lst[2 * i + 1]
        if tree[0][parent] == 0:
            tree[0][parent] = child
        else:
            tree[1][parent] = child

    findTree(N)

    print(f'#{test_case} {cnt}')
