import math

T = int(input())

for test_case in range(1, T + 1):
    result = []
    a, b = map(int, input().split())
    array = [True for _ in range(b)]
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(b))+1):
        if array[i]:
            j = 2
            while i * j < b:
                array[i * j] = False
                j += 1

    result = [i for i in range(len(array)) if array[i]]
    idx = 0
    for i in range(len(result)):
        if result[i] > a:
            idx = i
            break

    print(f'#{test_case} {sum(result[idx:])}')
