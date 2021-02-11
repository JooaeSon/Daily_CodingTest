def partition(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    L_lst = partition(lst[:mid])
    R_lst = partition(lst[mid:])

    return merge(L_lst, R_lst)


def merge(L_lst, R_lst):
    global cnt
    result = []

    L_len, R_len = len(L_lst), len(R_lst)
    L_idx, R_idx = 0, 0

    if L_lst[-1] > R_lst[-1]:
        cnt += 1

    while L_idx < L_len or R_idx < R_len:
        if L_idx < L_len and R_idx < R_len:  # 둘다 아직 남아있다면
            if L_lst[L_idx] <= R_lst[R_idx]:
                result.append(L_lst[L_idx])
                L_idx += 1
            else:
                result.append(R_lst[R_idx])
                R_idx += 1

        elif L_idx < L_len:  # 왼쪽이 남아있다면
            result.append(L_lst[L_idx])
            L_idx += 1

        elif R_idx < R_len:  # 오른쪽이 남아있다면
            result.append(R_lst[R_idx])
            R_idx += 1

    return result


T = int(input())

for test_case in range(1, T + 1):
    cnt = 0
    N = int(input())
    lst = list(map(int, input().split()))

    lst = partition(lst)
    print(f'#{test_case} {lst[N // 2]} {cnt}')
