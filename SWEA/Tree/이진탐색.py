def Tree(idx):
    global cnt

    if idx > N:
        return

    Tree(idx * 2)
    lst[idx] = cnt
    cnt += 1
    Tree(idx * 2 + 1)


T = int(input())

for test_case in range(1, T + 1):
    cnt = 1
    N = int(input())

    lst = [0] * (N + 1)
    Tree(1)

    print(f'#{test_case} {str(lst[1])} {str(lst[N // 2])}')
