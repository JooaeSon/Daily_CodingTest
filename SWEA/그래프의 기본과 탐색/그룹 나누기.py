def union(n1, n2):
    parents[findParent(n2)] = findParent(n1)


def findParent(num):
    if num == parents[num]:
        return num
    else:
        return findParent(parents[num])


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    inputData = list(map(int, input().split()))
    parents = [0] * (N + 1)

    for i in range(1, N + 1):
        parents[i] = i

    for i in range(M):
        union(inputData[i * 2], inputData[i * 2 + 1])

    result = set()
    for i in range(len(parents)):
        result.add(findParent(i))

    print(f'#{test_case} {len(result) - 1}')
