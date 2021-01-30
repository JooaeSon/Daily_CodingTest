T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    for i in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    for j in reversed(range(len(tree))):
        tree[j // 2] += tree[j]

    print(f'#{test_case} {tree[L]}')
