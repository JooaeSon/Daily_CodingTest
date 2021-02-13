def QuickSort(low, high):
    if low >= high:
        return

    pivot = low
    i, j = low + 1, high - 1

    while i <= j:
        while i <= j and A[i] <= A[pivot]: i += 1

        while i <= j and A[pivot] <= A[j]: j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]

    A[pivot], A[j] = A[j], A[pivot]

    QuickSort(low, j)
    QuickSort(j + 1, high)


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())

    A = list(map(int, input().split()))
    low, high = 0, len(A)
    QuickSort(low, high)

    print(f'#{test_case} {A[N // 2]}')
