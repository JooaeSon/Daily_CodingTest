T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lst = []
for i in range(1 << len(A)):
    sub_lst = []
    for j in range(len(A)):
        if i & 1 << j:  # 1비트열을 j번째로 이동
            sub_lst.append(A[j])
    lst.append(sub_lst)

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    result = 0
    for l in lst:
        if len(l) == N and sum(l) == K:
            result += 1

    print(f'#{test_case} {result}')