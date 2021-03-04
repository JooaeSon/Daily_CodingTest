
def PartitionSum(subset, K):

    Sum = sum(subset)
    if Sum < K: return 0
    elif Sum == K: return 1
    else:
        last = subset[-1]
        if last == K:
            return 1+PartitionSum(subset[:-1], K)
        else:
            if K-last > 0:
                return PartitionSum(subset[:-1], K-last)+PartitionSum(subset[:-1], K)
            else: # K<last
                return PartitionSum(subset[:-1], K)


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, K = map(int, input().split())
    subset = [i for i in range(1, N+1)]

    print(f'#{test_case} {PartitionSum(subset, K)}')
