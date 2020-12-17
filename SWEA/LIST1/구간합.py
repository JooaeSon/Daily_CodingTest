T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    sum_lst = []

    for i in range(len(lst)-M+1):
        sum_lst.append(sum(lst[i:i+M]))
    print(f'#{test_case} {max(sum_lst)-min(sum_lst)}')