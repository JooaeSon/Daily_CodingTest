T = int(input())

for test_case in range(1, T + 1):
    A = list(map(int, input().split()))
    LIS = [0] * len(A)

    for i in range(1, len(A)):
        LIS[i] = 1
        for j in range(1, i):
            if A[j] < A[i] and LIS[j] + 1 > LIS[i]:
                LIS[i] = LIS[j] + 1

    print(f'#{test_case} {max(LIS)}')