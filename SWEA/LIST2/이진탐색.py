def binarySearch(low, high, point):
    global cnt
    cnt = cnt+1
    center = int((low+high)/2)

    if point < center:
        return binarySearch(low, center, point)
    elif point > center:
        return binarySearch(center, high, point)
    else:
        return


T = int(input())

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    lst = []
    lst.append(A)
    lst.append(B)

    result = []
    for point in lst:
        low = 1
        high = P
        cnt = 0

        binarySearch(low, high, point)
        result.append(cnt)
    #print("result:", result)
    winner = ''
    if result[0] < result[1]:
        winner = 'A'
    elif result[0] > result[1]:
        winner = 'B'
    else:
        winner = str(0)

    print(f'#{test_case} {winner}')