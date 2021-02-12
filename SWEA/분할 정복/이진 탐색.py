T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    while B:
        num = B.pop()
        flag = 0
        L, R = 0, len(A) - 1

        while L <= R:
            M = (L + R) // 2

            if num == A[M]:
                result += 1
                break

            if num < A[M]:
                R = M - 1
                if flag == 1: break
                flag = 1
            elif num > A[M]:
                L = M + 1
                if flag == -1: break
                flag = -1

    print(f'#{test_case} {result}')
